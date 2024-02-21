import importlib
import os

from button import Button
from device import Device


class Seat:
    def __init__(self, seat_info, job):
        self.seat_name = seat_info.get("name")
        self.job = job
        self.devices = []

        self.primary_device = None
        self.keys = {}

        self.profile = None
        self.map = None
        self.map_fixed = None
        self.map_formatted = None

        self.target_file = None
        self.target_file_is_new = None

        device_key = seat_info.get("device")
        if device_key is not None:
            self.add_device(device_key, self.seat_name)

        multi_device = seat_info.get("devices")
        if multi_device is not None:
            for device_key, device_name in multi_device.items():
                self.add_device(device_key, device_name)

        if self.seat_name is None:
            self.seat_name = self.primary_device.name


    def add_device(self, device_key, device_name=None):
        module = importlib.import_module("devices." + device_key)
        for device_def in module.Devices.devices.values():
            device = Device(device_def, self, device_name)
            self.devices.append(device)

            # Seat primary device name
            if self.primary_device is None:
                self.primary_device = device

    def apply_profile(self, profile, ButtonClass: Button):
        self.keys = {}

        for device in self.devices:
            # Basic buttons
            buttons = device.definition.get("buttons")
            if buttons is not None:
                index = 0
                for button_key in buttons:
                    button = ButtonClass(button_key, device)
                    button.index = index
                    index = index + 1

                    # Map button names
                    button_names = device.definition.get("button_names")
                    if button_names is not None:
                        button_name = button_names.get(button_key)
                        if button_name is not None:
                            button.name = button_name

                    self.keys[button_key] = button

            # Axis
            sliders = device.definition.get("slider")
            if sliders is not None:
                axis_numbers = {}
                axis_number = 0
                for slider in sliders:
                    button_key = slider["name"]
                    button = ButtonClass(button_key, device)
                    button.set_slider(slider)

                    axis = slider["axis"]

                    button.axis_number = axis_numbers.get(axis)
                    if button.axis_number is None:
                        axis_numbers[axis] = axis_number
                        button.axis_number = axis_number
                        axis_number = axis_number + 1

                    self.keys[button_key] = button

            # Rumble
            rumble = device.definition.get("rumble")
            if rumble is not None:
                for button_key in rumble:
                    button = ButtonClass(button_key, device)
                    button.is_rumble = True
                    self.keys[button_key] = button

            accel = device.definition.get("Accelerometer")
            if accel is not None:
                for acc in accel:
                    button_key = acc["name"]
                    button = ButtonClass(button_key, device)
                    button.set_slider(acc)
                    button.is_accelerometer = True
                    self.keys[button_key] = button

            gyros = device.definition.get("Gyroscope")
            if gyros is not None:
                for gyro in gyros:
                    button_key = gyro["name"]
                    button = ButtonClass(button_key, device)
                    button.set_slider(gyro)
                    button.is_gyroscope = True
                    self.keys[button_key] = button

        # Setup profile
        self.profile = profile

        if self.job.install is True:
            target_dir = os.path.expanduser(profile.InstallDir)
            if hasattr(profile, "InstallFile"):
                self.target_file = os.path.join(target_dir, profile.InstallFile)
            else:
                self.target_file = os.path.join(target_dir, profile.TargetFile)
            if os.path.exists(self.target_file):
                self.target_file_is_new = False
            else:
                self.target_file_is_new = True
        else:
            target_dir = os.path.join('target', profile.TargetDir)
            self.target_file = os.path.join(target_dir, profile.TargetFile) + "-" + self.seat_name
            self.target_file_is_new = True

        if hasattr(profile, "get_profile_for_seat"):
            profile_data = profile.get_profile_for_seat(self)
            self.map = profile_data.get("map")
            self.map_fixed = profile_data.get("map_fixed")
            self.map_formatted = profile_data.get("map_formatted")
        else:
            self.map, self.map_fixed, self.map_formatted = None, None, None

        if self.map is None:
            self.map = profile.Map.copy()

        if self.map_fixed is None:
            if hasattr(profile, "FixedValues"):
                self.map_fixed = profile.FixedValues.copy()
            else:
                self.map_fixed = {}

        if self.map_formatted is None:
            if hasattr(profile, "FormattedValues"):
                self.map_formatted = profile.FormattedValues.copy()
            else:
                self.map_formatted = {}

        if not os.path.isdir(target_dir):
            os.mkdir(target_dir)

    def get_button_name_formatted(self, key, config_key):
        formatted = self.map_formatted.get(key)
        if formatted is not None:
            fstring = formatted[0]
            fvalues = []
            for i in range(1, len(formatted)):
                fkey = formatted[i]
                value = self.get_button_name(fkey, config_key)
                if value is None:
                    print(f"wrong parameter {fkey} for {key}")
                    return
                fvalues.append(value)
            return fstring.format(*fvalues)

    def get_button_name(self, key: None, config_key: None):
        button_name = None
        if key is not None:
            button_name = self.map_fixed.get(key)
            if button_name is None:
                button_name = self.get_button_name_formatted(key, config_key)
            if button_name is None:
                button = self.keys.get(key)
                if button is not None:
                    button_name = button.get_button_name()

        if button_name is None and config_key is not None:
            button_name = self.map_fixed.get(config_key)
            if button_name is None:
                button_name = self.get_button_name_formatted(config_key, config_key)
        return button_name
