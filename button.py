from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from device import Device


class Button:
    def __init__(self, name: str, device: Device):
        self.name: str = name
        self.index: int = 0
        self.device: Device = device

        self.is_slider: bool = False
        self.axis: int | None = None
        self.axis_number: int | None = None
        self.sign = None
        self.analog = None
        self.full = None
        self.is_rumble: bool = False
        self.is_accelerometer: bool = False
        self.is_gyroscope: bool = False
        self.calibrate: int = 1

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
