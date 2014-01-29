#! /usr/bin/env python

# Should be a Run pre-action along with a sleep 60

import os

home = os.environ['HOME']
#TODO figure out why transfer doesn't work. Try latest version
#os.system(home + '/.apportable/SDK/bin/transfer ~/tmp/PROJECTNAME-debug.apk')
os.system(home + '/.apportable/SDK/bin/adb install -r ~/tmp/PROJECTNAME-debug.apk')
os.system(home + '/.apportable/SDK/bin/adb shell am start -n com.apportable.PeevedPenguinsPaul/com.apportable.activity.VerdeActivity')