from __future__ import annotations

import yaml
from seat import Seat


class Job:
    def __init__(self):

        with open("config.yaml", "r") as file:
            self.config = yaml.safe_load(file)

        self.install: bool = self.config.get("install") or False
        self.seats: list[Seat] = []
        config_seats = self.config.get("seats")
        for config_seat in config_seats:
            self.seats.append(Seat(config_seat, self))
