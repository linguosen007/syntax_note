# subprocess sound

import sys
from subprocess import call
if sys.platform.startswith ('linux'):
    call(["xdg-open","sound.mp3"])
elif sys.platform.startswith('darwin'):
    call(["afplay","sound.mp3"])