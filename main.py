#!/usr/bin/python3

from job import Job
from profiles.dolphin import Dolphin
from profiles.dosbox import Dosbox
from profiles.mupen64plus import Mupen64

import sys

module = "help"
profile = ""
if len(sys.argv) > 1:
    module = sys.argv[1]
if len(sys.argv) > 2:
    profile = sys.argv[2]

if module == "help":
    print("Possible parameter: all dolphin dosbox mupen64")
    exit

job = Job()
if module == "dolphin" or module == "all":
    Dolphin(job).do_dolphin(profile)

if module == "dosbox" or module == "all":
    Dosbox(job).do_dosbox(profile)

if module == "mupen64" or module == "all":
    Mupen64(job).do_mupen64()
