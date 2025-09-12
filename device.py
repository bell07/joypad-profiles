class Device:
    def __init__(self, definition, seat, device_name: None):
        self.definition = definition
        self.seat = seat
        self.name: str = device_name or definition["name"]
        self.type = definition.get("device_type")
        self.js_number = 0
