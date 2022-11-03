class Button:
    def __init__(self, name, device):
        self.name = name
        self.index = None
        self.device = device

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
        fixed_value = self.device.seat.map_fixed.get(self.name)
        if fixed_value is not None:
            return fixed_value

        return self.name
