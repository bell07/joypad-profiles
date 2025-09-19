from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from job import Job


class Profile:
    def __init__(self, job: Job):
        self.job = job

    def run(self, profile_name: str) -> None:
        raise NotImplemented
