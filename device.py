import importlib
import os


class Button:
    def __init__(self, name, device):
        self.name = name
        self.index = None
        self.device = device
        self.device_name = None

        self.is_slider = False
        self.axis = None
        self.axis_number = None
        self.sign = None
        self.analog = None
        self.full = None
        self.is_rumble = False
        self.is_accelerometer = False
        self.is_gyroscope = False
        self.calibrate = 1

    def set_slider(self, slider):
        self.is_slider = True
        self.axis = slider.get("axis")
        self.sign = slider.get("sign")
        self.analog = slider.get("analog")
        self.full = slider.get("full")
        calibrate = slider.get("calibrate")
        if calibrate is not None:
            self.calibrate = calibrate

    def get_button_name(self):
        fixed_value = self.device.map_fixed.get(self.name)
        if fixed_value is not None:
            return fixed_value

        return self.name


class Device:
    def __init__(self, device, job, ButtonClass: Button):
        self.name = device.get("name")
        self.device_name = device.get("device_name")
        self.job = job
        self.keys = {}
        self.js_number = 0

        self.custom_attr = {}

        self.profile = None
        self.map = None
        self.map_fixed = None
        self.map_formatted = None
        self.target_file = None
        self.target_file_is_new = None

        self.has_imu = False
        self.has_l_imu = False
        self.has_r_imu = False

        device_map = device.get("device")
        cfg = importlib.import_module("devices." + device_map)

        if self.device_name is None:
            self.device_name = cfg.JS.name

        if self.name is None:
            self.name = self.device_name

        if self.name is None:
            print("ignoring Device without name")
            return
        index = 0
        for button_key in cfg.JS.buttons:
            button = ButtonClass(button_key, self)
            button.index = index
            index = index + 1

            if hasattr(cfg.JS, "button_names"):
                button_name = cfg.JS.button_names.get(button_key)
                if button_name is not None:
                    button.name = button_name

            self.keys[button_key] = button

        axis_numbers = {}
        axis_number = 0
        for slider in cfg.JS.slider:
            button_key = slider["name"]
            button = ButtonClass(button_key, self)
            button.set_slider(slider)

            axis = slider["axis"]

            button.axis_number = axis_numbers.get(axis)
            if button.axis_number is None:
                axis_numbers[axis] = axis_number
                button.axis_number = axis_number
                axis_number = axis_number + 1

            self.keys[button_key] = button

        if hasattr(cfg.JS, "rumble"):
            for button_key in cfg.JS.rumble:
                button = ButtonClass(button_key, self)
                button.is_rumble = True
                self.keys[button_key] = button

        if hasattr(cfg, "Pointer"):
            for button_key in cfg.Pointer.buttons:
                button = ButtonClass(button_key, self)
                button.device_name = cfg.Pointer.name
                self.keys[button_key] = button

            axis_numbers = {}
            axis_number = 0
            for slider in cfg.Pointer.slider:
                button_key = slider["name"]
                button = ButtonClass(button_key, self)
                button.set_slider(slider)
                button.device_name = cfg.Pointer.name
                axis = slider["axis"]

                button.axis_number = axis_numbers.get(axis)
                if button.axis_number is None:
                    axis_numbers[axis] = axis_number
                    button.axis_number = axis_number
                    axis_number = axis_number + 1
                self.keys[button_key] = button

        if hasattr(cfg, "IMU"):
            self.has_imu = True
            if hasattr(cfg.IMU, "Accelerometer"):
                for acc in cfg.IMU.Accelerometer:
                    button_key = acc["name"]
                    button = ButtonClass(button_key, self)
                    button.set_slider(acc)
                    button.is_accelerometer = True
                    button.device_name = cfg.IMU.name
                    self.keys[button_key] = button

            if hasattr(cfg.IMU, "Gyroscope"):
                for gyro in cfg.IMU.Gyroscope:
                    button_key = gyro["name"]
                    button = ButtonClass(button_key, self)
                    button.set_slider(gyro)
                    button.is_gyroscope = True
                    button.device_name = cfg.IMU.name
                    self.keys[button_key] = button

        if hasattr(cfg, "L_IMU"):
            self.has_l_imu = True
            if hasattr(cfg.L_IMU, "Accelerometer"):
                for acc in cfg.L_IMU.Accelerometer:
                    button_key = acc["name"]
                    button = ButtonClass(button_key, self)
                    button.set_slider(acc)
                    button.is_accelerometer = True
                    button.device_name = cfg.L_IMU.name
                    self.keys[button_key] = button

            if hasattr(cfg.L_IMU, "Gyroscope"):
                for gyro in cfg.L_IMU.Gyroscope:
                    button_key = gyro["name"]
                    button = ButtonClass(button_key, self)
                    button.set_slider(gyro)
                    button.is_gyroscope = True
                    button.device_name = cfg.L_IMU.name
                    self.keys[button_key] = button

        if hasattr(cfg, "R_IMU"):
            self.has_r_imu = True
            if hasattr(cfg.R_IMU, "Accelerometer"):
                for acc in cfg.R_IMU.Accelerometer:
                    button_key = acc["name"]
                    button = ButtonClass(button_key, self)
                    button.set_slider(acc)
                    button.is_accelerometer = True
                    button.device_name = cfg.R_IMU.name
                    self.keys[button_key] = button

            if hasattr(cfg.R_IMU, "Gyroscope"):
                for gyro in cfg.R_IMU.Gyroscope:
                    button_key = gyro["name"]
                    button = ButtonClass(button_key, self)
                    button.set_slider(gyro)
                    button.is_gyroscope = True
                    button.device_name = cfg.R_IMU.name
                    self.keys[button_key] = button

    def get_button(self, key):
        return self.keys.get(key)

    def apply_profile(self, profile):
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
            self.target_file = os.path.join(target_dir, profile.TargetFile) + "-" + self.name
            self.target_file_is_new = True

        if hasattr(profile, "get_profile_for_device"):
            profile_data = profile.get_profile_for_device(self)
            self.map = profile_data.get("map")
            self.map_fixed = profile_data.get("map_fixed")
            self.map_formatted = profile_data.get("map_formatted")

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
                button = self.get_button(key)
                if button is not None:
                    button_name = button.get_button_name()

        if button_name is None and config_key is not None:
            button_name = self.map_fixed.get(config_key)
            if button_name is None:
                button_name = self.get_button_name_formatted(config_key, config_key)
        return button_name
