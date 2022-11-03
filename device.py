class Device:
    def __init__(self, definition, seat, device_name: None):
        self.definition = definition
        self.seat = seat
        self.name = device_name
        self.type = definition.get("device_type")

        if self.name is None:
            self.name = definition.get("name")

        self.js_number = 0
