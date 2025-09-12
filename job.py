from __future__ import annotations

from seat import Seat
import yaml

seat_list = {
    "gpdwin2": {
        "devices": {
            "xpad_digital_trigger": "GPD Win 2 X-Box Controller",
            "touch_16_9": "Goodix Capacitive TouchScreen",
        }
    },
    "logitechF700": {
        "devices": {
            "xpad": "Logitech Gamepad F710"
        }
    },
    "nsw-pro": {
        "device": "nsw-pro"
    },
    "nsw-joycons": {
        "device": "nsw-joycons"
    },
    "hid-steamdeck": {
      "devices": {
          "hid-steamdeck": "Steam Deck",
          "touch_16_10": "FTS3528:00 2808:1015",
      }
    },
    "scc-steamdeck": {
        "name": "SCC SteamDeck",
        "devices": {
            "xpad": "Microsoft X-Box 360 pad",
            "touch_16_10": "FTS3528:00 2808:1015",
            "cemuhook": "SC-Controller",
            "scc-steamdeck": "SCController Keyboard"
        }
    }
}


class Job:
    def __init__(self):

        with open("config.yaml", 'r') as file:
            self.config = yaml.safe_load(file)

        self.install: bool = self.config.get("install") or False
        self.seats: list[Seat] = []
        if self.config.get("all_seats"):
            for seat_key in seat_list:
                self.seats.append(Seat(seat_list[seat_key], self))

        config_seats = self.config.get("seats")
        if config_seats:
            for config_seat in config_seats:
                seat_key = config_seat.get("seat")
                if seat_key:
                    seat_info = seat_list[seat_key].copy()
                else:
                    seat_info = {}
                
                seat_name = config_seat.get("seat_name")
                if seat_name:
                    seat_info["name"] = seat_name

                config_devices = config_seat.get("devices")
                if config_devices:
                    for config_device in config_devices:
                        device = config_device.get("device")
                        assert device
                        device_name = config_device.get("device_name")
                        if not device_name:
                            seat_info["device"] = device
                            break

                        if not seat_info.get("devices"):
                            seat_info["devices"] = {}
                        seat_info["devices"][device] = device_name

                self.seats.append(Seat(seat_info, self))

