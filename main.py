#!/usr/bin/python3

import sys

from job import Job
from profiles.dolphin import Dolphin
from profiles.dosbox import Dosbox

module: str = "help"
profile: str = "all"
if len(sys.argv) > 1:
    module = sys.argv[1]
if len(sys.argv) > 2:
    profile = sys.argv[2]

if module == "help":
    print("Possible parameter: all dolphin dosbox mupen64")
    exit()

job = Job()
if module == "dolphin" or module == "all":
    Dolphin(job).do_dolphin(profile)

if module == "dosbox" or module == "all":
    Dosbox(job).do_dosbox(profile)
