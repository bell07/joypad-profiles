from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from seat import Seat


class Device:
    def __init__(self, definition, seat: Seat, device_name: str | None = None):
        self.definition = definition
        self.seat: Seat = seat
        self.name: str = device_name or definition["name"]
        self.type: str = definition.get("device_type")
        self.js_number = 0
