# Mupen64 N64 profile

import configparser

from button import Button


class Profile:
    TargetDir = "mupen64plus"
    InstallDir = "~/.config/mupen64plus"
    TargetFile = "mupen64plus.cfg"

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
        ["B Button", "WEST"],
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
    def get_profile_for_seat(seat):
        ret_map = []
        for line in Profile.Map:
            if len(line) > 1 and line[1] == "_NOUPDATE_":
                if seat.target_file_is_new is True:
                    ret_map.append([line[0]])
                continue
            ret_map.append(line)

        map_fixed = Profile.FixedValues.copy()
        map_fixed["device"] = seat.primary_device.js_number
        map_fixed["name"] = '"' + seat.primary_device.name + '"'

        left = seat.keys.get("LS_LEFT")
        right = seat.keys.get("LS_RIGHT")
        map_fixed["X Axis"] = f'"axis({str(left.axis_number)}{left.sign},{str(right.axis_number)}{right.sign})"'

        up = seat.keys.get("LS_UP")
        down = seat.keys.get("LS_DOWN")
        map_fixed["Y Axis"] = f'"axis({str(up.axis_number)}{up.sign},{str(down.axis_number)}{down.sign})"'

        return {"map": ret_map, "map_fixed": map_fixed}


class MupenButton(Button):
    def __init__(self, name, device):
        super().__init__(name, device)

    def get_button_name(self):
        if self.device.type != 'joypad':
            print(f'Button {self.name}',
                  f'from device {self.device.name} type {self.device.type}'
                  f'not supported in dosbox profile generator')
            return ''

        if self.is_slider is True:
            if self.name[0:4] == "DPAD":
                return '"hat(0 ' + self.name[5:6].upper() + self.name[6:].lower() + ')"'
            else:
                return '"axis(' + str(self.axis_number) + self.sign + ')"'
        else:
            return '"button(' + str(self.index) + ')"'


class Mupen64:
    def __init__(self, job):
        self.job = job

    def do_mupen64(self):
        for seat in self.job.seats:
            seat.apply_profile(Profile, MupenButton)

            # Read current file, check the input section version
            config = configparser.ConfigParser(allow_no_value=True)
            config.optionxform = str
            config.read(seat.target_file)

            mupen64plus_config_section_name = "Input-SDL-Control1"  # Only 1 player supported
            if not config.has_section(mupen64plus_config_section_name):
                config.add_section(mupen64plus_config_section_name)
            section = config[mupen64plus_config_section_name]

            for line in seat.map:
                config_key = line[0]
                key = None
                if len(line) > 1:
                    key = line[1]

                parsed = seat.get_button_name(key, config_key)
                if parsed is not None:
                    section[config_key] = parsed

            # Save file
            with open(seat.target_file, 'w') as configfile:
                print(f"update config file {seat.target_file}")
                config.write(configfile)
