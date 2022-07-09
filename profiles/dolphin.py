import os
import configparser
from device import Button, Device

from profiles.dolphin_profiles import GCPad, Horizontal, Nunchuk

# Supported rumble types
Rumble = {
    "TRIANGLE": "Triangle",
    "SQUARE": "Square",
    "SINE": "Sine",
}

VirtualPointer = {
    # Virtual X pointer
    "CLICK_LEFT": "`XInput2/0/Virtual core pointer:Click 1`",
    "CLICK_MIDDLE": "`XInput2/0/Virtual core pointer:Click 2`",
    "CLICK_RIGHT": "`XInput2/0/Virtual core pointer:Click 3`",
    "POINTER_UP": "`XInput2/0/Virtual core pointer:Cursor Y-`",
    "POINTER_DOWN": "`XInput2/0/Virtual core pointer:Cursor Y+`",
    "POINTER_LEFT": "`XInput2/0/Virtual core pointer:Cursor X-`",
    "POINTER_RIGHT": "`XInput2/0/Virtual core pointer:Cursor X+`",
}


class DolphinButton(Button):
    def get_button_name(self):
        device = ""
        if self.device_name is not None:
            device = f"evdev/0/{self.device_name}:"

        if self.is_accelerometer is True:
            slider_name = "Accel " + self.axis + self.sign
            return f"`{device + slider_name}`"

        elif self.is_gyroscope is True:
            slider_name = "Gyro " + self.axis + self.sign
            return f"`{device + slider_name}`"

        elif self.is_slider is True:
            slider_name = "Axis " + str(self.axis_number) + self.sign
            if self.full is True:
                slider_name = "Full " + slider_name
            slider_name = f"`{device + slider_name}`"
            if self.calibrate != 1:
                slider_name = f"({slider_name} * {str(self.calibrate)})"
            return slider_name

        elif self.is_rumble:
            return Rumble[self.name]

        else:
            button_name = super().get_button_name()
            if device != "" and button_name is not None:
                button_name = f"`{device + button_name}`"

            if self.name == "TOUCH":
                button_name = f"tap({button_name},0.5)"

            return button_name


class Dolphin:
    def __init__(self, job):
        self.job = job
        if job.install is True:
            # Target dirs for current user
            self.DOLPHIN_PATH = os.path.expanduser('~/.config/dolphin-emu')
            self.PROFILES_PATH = os.path.join(self.DOLPHIN_PATH, "Profiles")
            self.GAME_SETTINGS = os.path.expanduser("~/.local/share/dolphin-emu/GameSettings")
        else:
            # Current dir
            self.DOLPHIN_PATH = os.path.join('target', 'dolphin-emu')
            self.PROFILES_PATH = os.path.join(self.DOLPHIN_PATH, "Profiles")
            self.GAME_SETTINGS = os.path.join(self.DOLPHIN_PATH, "GameSettings")

        if not os.path.isdir(self.DOLPHIN_PATH):
            print(self.DOLPHIN_PATH + " not found. Skip dolphin configuration")
            # TODO error handling
        if not os.path.isdir(self.PROFILES_PATH):
            os.mkdir(self.PROFILES_PATH)

        wiimote_path = os.path.join(self.PROFILES_PATH, "Wiimote")
        if not os.path.isdir(wiimote_path):
            os.mkdir(wiimote_path)

        gcpad_path = os.path.join(self.PROFILES_PATH, "GCPad")
        if not os.path.isdir(gcpad_path):
            os.mkdir(gcpad_path)

        if not os.path.isdir(self.GAME_SETTINGS):
            os.mkdir(self.GAME_SETTINGS)

    def get_parsed_value(self, device, config_key, param):
        #  Button string to be mapped
        if param is None:
            key_name = device.get_button_name(param, config_key)
            if key_name is None:
                print(f"Device {device.name} does not map {config_key}")
            else:
                return key_name

        elif type(param) == str:
            key_name = device.get_button_name(param, config_key)
            if key_name is None:
                print(f"Device {device.name} does not know {param}")
            else:
                return key_name

        #  Buttons list to be mapped recursively and connect by " | " (or)
        elif type(param) == list:
            parsed_data = None
            for button_key in param:
                parsed_element = self.get_parsed_value(device, config_key, button_key)
                if parsed_element is not None:
                    if parsed_data is None:
                        parsed_data = parsed_element
                    else:
                        parsed_data = parsed_data + ' | ' + parsed_element
            return parsed_data

    @staticmethod
    def adjust_rumble(device, map_fixed):
        for rumble in Rumble:
            if device.get_button(rumble):
                rumble_name = Rumble.get(rumble)
                break
        map_fixed["Rumble/Motor"] = rumble_name

    def get_profile(self, device, profile):
        data = "Device = " + "evdev/" + str(device.js_number) + "/" + device.name + "\n"

        device.apply_profile(profile)
        self.adjust_rumble(device, device.map_fixed)

        if device.get_button("TOUCH") is None:
            for key in VirtualPointer:
                device.map_fixed[key] = VirtualPointer[key]

        if device.has_imu == False:
            device.map_fixed["IMUIR/Enabled"] = None

        for line in device.map:
            line_copy = line.copy()
            config_key = line_copy.pop(0)
            if len(line_copy) == 0:
                line_copy = None
            parsed_value = self.get_parsed_value(device, config_key, line_copy)
            if parsed_value is not None:
                data = data + config_key + " = " + parsed_value + "\n"

        return data

    def do_config(self, device, profile):
        file_content = self.get_profile(device, profile)

        if self.job.install is True:
            file_name = os.path.join(self.PROFILES_PATH, profile.Type, profile.ProfileName + ".ini")
        else:
            file_name = os.path.join(self.PROFILES_PATH, profile.Type, profile.ProfileName + ".ini-" + device.name)
        print("Write " + file_name)
        f = open(file_name, "w")
        f.write("[Profile]" + "\n" + file_content)
        f.close()

        # Apply to WII games
        if hasattr(profile, "Games"):
            for game in profile.Games:
                game_config = configparser.ConfigParser(allow_no_value=True)
                game_config.optionxform = str
                game_config_file = os.path.join(self.GAME_SETTINGS, game + ".ini")
                game_config.read(game_config_file)

                if not game_config.has_section("Controls"):
                    game_config.add_section("Controls")
                section = game_config["Controls"]

                section["WiimoteProfile1"] = profile.ProfileName
                with open(game_config_file, 'w') as configfile:
                    print(f"update {game_config_file} for {profile.ProfileName}")
                    game_config.write(configfile)

        return file_content  # Return to concatenate into default config

    def do_dolphin(self):
        def_gc = ""
        def_wii = ""

        for device_info in self.job.devices:
            device = Device(device_info, DolphinButton)

            #  Do GameCube config for the Seat
            file_content = self.do_config(device, GCPad)
            def_gc = def_gc + "[GCPad1]" + "\n" + file_content + "\n"
            self.do_config(device, GCPad)

            #  Do WII horizontal
            file_content = self.do_config(device, Horizontal)
            def_wii = def_wii + "[Wiimote1]" + "\n" + file_content + "\n"

            # Do WII with Nunchuk
            self.do_config(device, Nunchuk)

            if self.job.install is True:
                #  Write default GC config
                file_name = os.path.join(self.DOLPHIN_PATH, "GCPadNew.ini")
                print("Write " + file_name)
                f = open(file_name, "w")
                f.write(def_gc)
                f.close()

                #  Write default Wiimote config
                file_name = os.path.join(self.DOLPHIN_PATH, "WiimoteNew.ini")
                print("Write " + file_name)
                f = open(file_name, "w")
                f.write(def_wii)
                f.close()
