from settings import Settings

devices_list = {
    "gpdwin2": {
        "device": "gpdwin2"
    },
    "logitechF700": {
        "device_name": "Logitech Gamepad F710",
        "device": "xpad"
    },
    "nsw-pro": {
        "device": "nsw-pro"
    },
    "nsw-joycons": {
        "device": "nsw-joycons"
    },
}


class Job:
    def __init__(self):
        self.install = Settings.install
        self.devices = []

        if Settings.device == "all":
            for key, values in devices_list.items():
                self.devices.append(values)
        else:
            device = devices_list[Settings.device]
            if device is None:
                device = {"device": Settings.device}

            if hasattr(Settings, "name"):
                device["name"] = Settings.get("name")

            if hasattr(Settings, "device_name"):
                device["device_name"] = Settings.get("device_name")

            self.devices.append(device)
