from job import Job
from profiles.dolphin import Dolphin
from profiles.mupen64plus import Mupen64

job = Job()
Dolphin(job).do_dolphin()
Mupen64(job).do_mupen64()
