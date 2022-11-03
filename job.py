from seat import Seat
from settings import Settings

seat_list = {
    "gpdwin2": {
        "device": "gpdwin2"
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
}


class Job:
    def setup_seat(self, seat_key, seat_info):
        name = seat_info.get("name")
        seat = Seat(self, name)

        device_key = seat_info.get("device")
        if device_key is not None:
            seat.add_device(device_key, seat)

        multi_device = seat_info.get("devices")
        if multi_device is not None:
            for device_key, device_name in multi_device.items():
                seat.add_device(device_key, seat, device_name)

        return seat

    def __init__(self):
        self.install = Settings.install
        self.seats = []

        if hasattr(Settings, "seat") and Settings.seat == "all":
            for seat_key, seat_info in seat_list.items():
                self.seats.append(self.setup_seat(seat_key, seat_info))

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

            self.seats.append(self.setup_seat(seat_key, seat_info))
