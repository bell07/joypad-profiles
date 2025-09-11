from seat import Seat
from settings import Settings

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
        self.install = Settings.install
        self.seats = []

        if hasattr(Settings, "seat") and Settings.seat == "all":
            for seat_key, seat_info in seat_list.items():
                self.seats.append(Seat(seat_info, self))

        else:
            # Compose 1 seat by all data
            seat_key = None
            seat_info = {}

            if hasattr(Settings, "name"):
                seat_info["name"] = Settings.name

            if hasattr(Settings, "seat"):
                seat_key = Settings.seat
                seat_info = seat_list[Settings.seat]

            if hasattr(Settings, "device_name"):
                d = seat_info.get("devices")
                if d is None:
                    seat_info["devices"] = {Settings.device: Settings.device_name}
                else:
                    seat_info["devices"] = d + {Settings.device: Settings.device_name}

            elif hasattr(Settings, "device"):
                seat_info["device"] = Settings.device

            if hasattr(Settings, "devices"):
                d = seat_info.get("devices")
                if d is None:
                    seat_info["devices"] = Settings.devices
                else:
                    seat_info["devices"] = d + Settings.devices

            self.seats.append(Seat(seat_info, self))
