import os
from device import Button, Device
from profiles.dosbox_profiles import \
    digger, \
    tombraider, \
    turrican2

DOSGAMES_PATH = "~/Games/DOS/"

dpad_map = {
    "DPAD_UP": ' hat 0 1"',
    "DPAD_DOWN": ' hat 0 4"',
    "DPAD_LEFT": ' hat 0 8"',
    "DPAD_RIGHT": ' hat 0 2"',
}


class DosboxButton(Button):
    def get_button_name(self):
        name = '"stick_' + str(self.device.js_number)
        dpad_name = dpad_map.get(self.name)
        if dpad_name is not None:
            return name + dpad_name

        if self.is_slider is True:
            return name + ' axis ' + str(self.axis_number) + " " + ("0" if self.sign == '-' else "1") + '"'
        else:
            return name + ' button ' + str(self.index) + '"'


class DosboxProfile:
    def __init__(self, profile, variant):
        self.Map = profile.Map

        if variant == "dosbox":
            self.TargetDir = "dosbox"
            self.TargetFile = profile.GameName + ".map"
            self.InstallDir = os.path.expanduser(DOSGAMES_PATH + profile.GameName)
            self.InstallFile = "dosbox-mapper.map"

        elif variant == "dosbox-x":
            self.TargetDir = "dosbox-x"
            self.TargetFile = profile.GameName + ".map"
            self.InstallDir = os.path.expanduser(DOSGAMES_PATH + profile.GameName)
            self.InstallFile = "dosbox-x-mapper.map"


class Dosbox:
    def __init__(self, job):
        self.job = job

    @staticmethod
    def get_parsed_value(device, config_key, param):
        parsed_data = None
        for button_key in param:
            parsed_element = device.get_button_name(button_key, config_key)
            if parsed_element is None:
                print(f"Device {device.name} does not know {param}")

            if parsed_element is not None:
                if parsed_data is None:
                    parsed_data = parsed_element
                else:
                    parsed_data = parsed_data + ' ' + parsed_element
        return parsed_data

    def do_config(self, device_info, profile, variant):
        device = Device(device_info, self.job, DosboxButton)
        device.apply_profile(DosboxProfile(profile, variant))
        print("Write " + device.target_file)
        sf, tf = None, None
        if variant == "dosbox":
            sf = open(os.path.join(os.path.dirname(__file__), "dosbox_profiles", "mapper-doxbox-sdl2-0.78.1.map"))
            tf = open(device.target_file, 'w')
        elif variant == "dosbox-x":
            sf = open(os.path.join(os.path.dirname(__file__), "dosbox_profiles", "mapper-dosbox-x-sdl2-2022.08.0.map"))
            tf = open(device.target_file, 'w')

        map_dct = {}
        for map_line in device.map:
            line_copy = map_line.copy()
            config_key = line_copy.pop(0)
            parsed_value = self.get_parsed_value(device, config_key, line_copy)
            map_dct[config_key] = parsed_value

        for line in sf.readlines():
            if line[0:1] == "j":  # Ignore joystick keys
                continue

            split = line.split(" ", 2)
            config_key = split.pop(0)
            config_entry = map_dct.get(config_key)
            if config_entry is None:
                tf.write(line)
            else:
                tf.write(config_key + " " + config_entry + " " + " ".join(split))

        sf.close()
        tf.close()

    def do_dosbox(self):
        for device_info in self.job.devices:
            self.do_config(device_info, digger, "dosbox")
            self.do_config(device_info, digger, "dosbox-x")

            self.do_config(device_info, tombraider, "dosbox")
            self.do_config(device_info, tombraider, "dosbox-x")

            self.do_config(device_info, turrican2, "dosbox")
            self.do_config(device_info, turrican2, "dosbox-x")
