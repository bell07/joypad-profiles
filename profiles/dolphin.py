import configparser
import os

from button import Button
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

DSUClientNames = {
    "ACCEL_UP": "Accel Up",
    "ACCEL_DOWN": "Accel Down",
    "ACCEL_FORWARD": "Accel Forward",
    "ACCEL_BACKWARD": "Accel Backward",
    "ACCEL_LEFT": "Accel Left",
    "ACCEL_RIGHT": "Accel Right",
    "ROLL_LEFT": "Gyro Roll Left",
    "ROLL_RIGHT": "Gyro Roll Right",
    "PITCH_UP": "Gyro Pitch Up",
    "PITCH_DOWN": "Gyro Pitch Down",
    "YAW_LEFT": "Gyro Yaw Left",
    "YAW_RIGHT": "Gyro Yaw Right",
}


class DolphinButton(Button):
    def get_button_name(self):
        device = ""
        device_type = "evdev"

        if self.device.name != self.device.seat.primary_device.name:
            if self.device.type == "DSUClient":
                device_type = "DSUClient"
            device = f"{device_type}/0/{self.device.name}:"

        if self.device.type == "DSUClient":
            slider_name = DSUClientNames.get(self.name)
            if slider_name is None:
                return
            else:
                return f"`{device}{slider_name}`"

        if self.is_accelerometer is True:
            slider_name = "Accel " + self.axis + self.sign
            return f"`{device}{slider_name}`"

        elif self.is_gyroscope is True:
            slider_name = "Gyro " + self.axis + self.sign
            return f"`{device}{slider_name}`"

        elif self.is_slider is True:
            slider_name = "Axis " + str(self.axis_number) + self.sign
            if self.full is True:
                slider_name = "Full " + slider_name
            slider_name = f"`{device}{slider_name}`"
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
            # Default settings and Game settings target dir
            self.DEFCONFIG_PATH = os.path.expanduser('~/.config/dolphin-emu')
            self.GAME_SETTINGS = os.path.expanduser("~/.local/share/dolphin-emu/GameSettings")
        else:
            # GameSettings in target folder
            self.DEFCONFIG_PATH = None
            self.GAME_SETTINGS = os.path.join("target", "dolphin-emu", "GameSettings")

        os.makedirs(self.GAME_SETTINGS, exist_ok=True)

    def get_parsed_value(self, seat, config_key, param):
        #  Button string to be mapped
        if param is None:
            key_name = seat.get_button_name(param, config_key)
            if key_name is None:
                print(f"Device {seat.seat_name} does not map {config_key}")
            else:
                return key_name

        elif type(param) == str:
            key_name = seat.get_button_name(param, config_key)
            if key_name is None:
                print(f"Device {seat.seat_name} does not know {param}")
            else:
                return key_name

        #  Buttons list to be mapped recursively and connect by " | " (or)
        elif type(param) == list:
            parsed_data = None
            for button_key in param:
                parsed_element = self.get_parsed_value(seat, config_key, button_key)
                if parsed_element is not None:
                    if parsed_data is None:
                        parsed_data = parsed_element
                    else:
                        parsed_data = parsed_data + ' | ' + parsed_element
            return parsed_data

    @staticmethod
    def adjust_rumble(seat, map_fixed):
        rumble_name = None
        for rumble in Rumble:
            if seat.keys.get(rumble):
                rumble_name = Rumble.get(rumble)
                break
        map_fixed["Rumble/Motor"] = rumble_name

    def get_profile(self, seat):
        data = "Device = " + "evdev/" + str(seat.primary_device.js_number) + "/" + seat.primary_device.name + "\n"

        self.adjust_rumble(seat, seat.map_fixed)

        if seat.keys.get("TOUCH") is None:
            for key in VirtualPointer:
                seat.map_fixed[key] = VirtualPointer[key]

        if seat.keys.get("ACCEL_UP") is not None or seat.keys.get("L_ACCEL_UP") is not None \
                or seat.keys.get("R_ACCEL_UP") is not None:
            # If Touchscreen available, the device is a handheald. IMUIR emulation is designed for joypad + TV
            if seat.keys.get("TOUCH"):
                seat.map_fixed["IMUIR/Enabled"] = "False"
            pass
        else:
            # No Gyro available for IMUIR emulation
            seat.map_fixed["IMUIR/Enabled"] = "False"

        for line in seat.map:
            line_copy = line.copy()
            config_key = line_copy.pop(0)
            if len(line_copy) == 0:
                line_copy = None
            parsed_value = self.get_parsed_value(seat, config_key, line_copy)
            if parsed_value is not None:
                data = data + config_key + " = " + parsed_value + "\n"

        return data

    def do_config(self, seat, profile):
        seat.apply_profile(profile, DolphinButton)
        file_content = self.get_profile(seat)

        print("Write " + seat.target_file)
        f = open(seat.target_file, "w")
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

                target_profile = profile.TargetFile[0:-4]
                section["WiimoteProfile1"] = target_profile
                with open(game_config_file, 'w') as configfile:
                    print(f"update {game_config_file} for {target_profile}")
                    game_config.write(configfile)

        return file_content  # Return to concatenate into default config

    def do_dolphin(self, profile_name):

        if profile_name == "help":
            print("Possible dolphin parameter: all, GCPad, Horizontal, Nunchuk")
            return

        def_gc = ""
        def_wii = ""

        for seat in self.job.seats:
            if seat.seat_name == "Steam Deck":
                print("hid-steamdeck not implemented for dolphin beacause it uses not the evdev driver")
                continue

            if profile_name == "GCPad" or profile_name == "all":
                #  Do GameCube config for the Seat
                file_content = self.do_config(seat, GCPad)
                def_gc = def_gc + "[GCPad1]" + "\n" + file_content + "\n"

                if self.DEFCONFIG_PATH is not None:
                    #  Write default GC config
                    file_name = os.path.join(self.DEFCONFIG_PATH, "GCPadNew.ini")
                    print("Write " + file_name)
                    f = open(file_name, "w")
                    f.write(def_gc)
                    f.close()

            #  Do WII horizontal
            if profile_name == "Horizontal" or profile_name == "all":
                file_content = self.do_config(seat, Horizontal)
                def_wii = def_wii + "[Wiimote1]" + "\n" + file_content + "\n"
                if self.DEFCONFIG_PATH is not None:
                    #  Write default Wiimote config
                    file_name = os.path.join(self.DEFCONFIG_PATH, "WiimoteNew.ini")
                    print("Write " + file_name)
                    f = open(file_name, "w")
                    f.write(def_wii)
                    f.close()

            # Do WII with Nunchuk
            if profile_name == "Nunchuk" or profile_name == "all":
                self.do_config(seat, Nunchuk)

            for device in seat.devices:
                if device.type == "DSUClient":
                    print(f'>>> Please configure DSU Client "{device.name}" in Dolphin settings')
