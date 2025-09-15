from __future__ import annotations

import importlib
import os
from typing import TYPE_CHECKING, Any, Type

from button import Button
from device import Device

if TYPE_CHECKING:
    from job import Job


class Seat:
    def __init__(self, seat_info: dict[str, Any], job: Job):

        self.job: Job = job
        self.devices: list[Device] = []

        self.primary_device: Device
        self.keys: dict[str, Button] = {}

        self.profile = None  # TODO Profile typing
        self.map: list[list[str]] = []
        self.map_fixed: dict = {}
        self.map_formatted: dict[str, str] = {}

        self.target_file: str
        self.target_file_is_new: bool

        seat_name: str | None = seat_info.get("name")

        device_key = seat_info.get("device")
        if device_key:
            self.add_device(device_key, seat_name)

        multi_device: dict[str, str] | None = seat_info.get("devices")
        if multi_device:
            for device_key, device_name in multi_device.items():
                self.add_device(device_key, device_name)

        assert self.primary_device
        self.seat_name: str = seat_name or self.primary_device.name

    def add_device(self, device_key, device_name=None) -> None:
        module = importlib.import_module("devices." + device_key)
        for device_def in module.Devices.devices.values():
            device = Device(device_def, self, device_name)
            self.devices.append(device)

            # Seat primary device name
            if len(self.devices) == 1:
                self.primary_device = device

    def apply_profile(self, profile, ButtonClass: Type[Button]):
        self.keys = {}

        for device in self.devices:
            # Basic buttons
            buttons = device.definition.get("buttons")
            if buttons is not None:
                index = 0
                for button_key in buttons:
                    button = ButtonClass(button_key, device)
                    if device.type == "joypad":
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
            target_dir = os.path.join("target", profile.TargetDir)
            os.makedirs(target_dir, exist_ok=True)
            self.target_file = (
                os.path.join(target_dir, profile.TargetFile) + "-" + self.seat_name
            )
            self.target_file_is_new = True

        if hasattr(profile, "get_profile_for_seat"):
            profile_data = profile.get_profile_for_seat(self)
            self.map = profile_data.get("map") or []
            self.map_fixed = profile_data.get("map_fixed") or {}
            self.map_formatted = profile_data.get("map_formatted") or {}
        else:
            self.map, self.map_fixed, self.map_formatted = [], {}, {}

        if len(self.map) == 0:
            self.map = profile.Map.copy()

        if not self.map_fixed:
            if hasattr(profile, "FixedValues"):
                self.map_fixed = profile.FixedValues.copy()

        if not self.map_formatted:
            if hasattr(profile, "FormattedValues"):
                self.map_formatted = profile.FormattedValues.copy()

    def get_button_name_formatted(self, key: str, config_key: str | None) -> str | None:
        formatted = self.map_formatted.get(key)
        if formatted is not None:
            fstring = formatted[0]
            fvalues = []
            for i in range(1, len(formatted)):
                fkey: str = formatted[i]
                value = self.get_button_name(fkey, config_key)
                if value is None:
                    print(f"wrong parameter {fkey} for {key}")
                    return
                fvalues.append(value)
            return fstring.format(*fvalues)

    def get_button_name(
        self, key: str | None = None, config_key: str | None = None
    ) -> str | None:
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
