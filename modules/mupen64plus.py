import configparser
import os
from device import Button, Device


class Profile:
    Map = [
        ["version", "_NOUPDATE_"],
        ["mode"],
        ["device"],
        ["name"],
        ["plugged"],
        ["plugin", "_NOUPDATE_"],
        ["mouse", "_NOUPDATE_"],
        ["MouseSensitivity", "_NOUPDATE_"],
        ["AnalogDeadzone", "_NOUPDATE_"],
        ["AnalogPeak", "_NOUPDATE_"],
        ["DPad R", "DPAD_RIGHT"],
        ["DPad L", "DPAD_LEFT"],
        ["DPad D", "DPAD_DOWN"],
        ["DPad U", "DPAD_UP"],
        ["Start", "START"],
        ["Z Trig", "TL2"],
        ["B Button", "NORTH"],
        ["A Button", "SOUTH"],
        ["C Button R", "RS_RIGHT"],
        ["C Button L", "RS_LEFT"],
        ["C Button D", "RS_DOWN"],
        ["C Button U", "RS_UP"],
        ["R Trig", "TR"],
        ["L Trig", "TL"],
        ["Mempak switch", "SELECT"],
        ["Rumblepak switch", "TR2"],
        ["X Axis"],
        ["Y Axis"]
    ]

    FixedValues = {
        "version": "2,000000",
        "mode": "0",
        "plugged": "True",
        "plugin": "2",
        "mouse": "False",
        "MouseSensitivity": '"2,00,2,00"',
        "AnalogDeadzone": '"4096,4096"',
        "AnalogPeak": '"32768,32768"',
    }

    @staticmethod
    def get_profile_for_device(device):
        new_config = device.custom_attr.get("new_config")
        ret_map = []
        for line in Profile.Map:
            if len(line) > 1 and line[1] == "_NOUPDATE_":
                if new_config == True:
                    ret_map.append([line[0]])
                continue
            ret_map.append(line)

        map_fixed = Profile.FixedValues.copy()
        map_fixed["device"] = device.js_number
        map_fixed["name"] = '"' + device.name + '"'

        left = device.get_button("DPAD_LEFT")
        right = device.get_button("DPAD_RIGHT")
        map_fixed["X Axis"] = '"' + "axis(" + str(left.hat) + left.sign + "," + str(right.hat) + right.sign + ")" + '"'

        up = device.get_button("DPAD_UP")
        down = device.get_button("DPAD_DOWN")
        map_fixed["Y Axis"] = '"' + "axis(" + str(up.hat) + up.sign + "," + str(down.hat) + down.sign + ")" + '"'

        return {"map": ret_map, "map_fixed": map_fixed}


HatMap = {
    "DPAD_RIGHT": 0,
    "DPAD_LEFT": 0,
    "DPAD_DOWN": 1,
    "DPAD_UP": 1,
}


class MupenButton(Button):
    def __init__(self, name, device):
        super().__init__(name, device)
        self.hat = HatMap.get(name)

    def get_button_name(self):
        if self.is_slider is True:
            if self.hat is not None:
                return '"hat(' + str(self.device.js_number) + " " \
                       + self.name[5:6].upper() + self.name[6:].lower() + ')"'
            else:
                return '"axis(' + str(self.axis_number) + self.sign + ')"'
        else:
            return '"button(' + str(self.index) + ')"'


class Mupen64:
    def __init__(self, job):
        self.job = job
        if job.install is True:
            self.config_dir = os.path.expanduser("~/.config/mupen64plus")
        else:
            self.config_dir = os.path.join('target', 'mupen64plus')

        if not os.path.isdir(self.config_dir):
            os.mkdir(self.config_dir)

    def do_mupen64(self):
        for device_info in self.job.devices:
            device = Device(device_info, MupenButton)

            if len(self.job.devices) > 1:
                self.config_file = os.path.join(self.config_dir, "mupen64plus.cfg-" + device.name)
            else:
                self.config_file = os.path.join(self.config_dir, "mupen64plus.cfg")

            # Read current file, check the input section version
            config = configparser.ConfigParser(allow_no_value=True)
            config.optionxform = str
            config.read(self.config_file)

            mupen64plus_config_section_name = "Input-SDL-Control1"  # Only 1 player supported
            new_config = False
            if not config.has_section(mupen64plus_config_section_name):
                config.add_section(mupen64plus_config_section_name)
                new_config = True
            section = config[mupen64plus_config_section_name]

            device = Device(device_info, MupenButton)
            device.custom_attr["new_config"] = new_config
            device.apply_profile(Profile)

            for line in device.map:
                config_key = line[0]
                key = None
                if len(line) > 1:
                    key = line[1]

                parsed = device.get_button_name(key, config_key)
                if parsed is not None:
                    section[config_key] = parsed

            # Save file
            with open(self.config_file, 'w') as configfile:
                print(f"update config file {self.config_file}")
                config.write(configfile)
