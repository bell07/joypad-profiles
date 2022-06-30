from job import Job
from modules.dolphin import Dolphin
from modules.mupen64plus import Mupen64

job = Job()
Dolphin(job).do_dolphin()
Mupen64(job).do_mupen64()
