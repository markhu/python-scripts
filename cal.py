#!/usr/bin/env python

# cal.py
# emulate the original Unix `cal` command

# TBD: highlight the current day (cross-platform Linux + Windows)

import sys

import calendar
import time   # simpler than datetime

calendar.setfirstweekday(calendar.SUNDAY)

if len(sys.argv) == 2:
    Y = sys.argv[1]
    calendar.prcal(int(Y))
elif len(sys.argv) == 3:
    Y = sys.argv[1]
    m = sys.argv[2]
    calendar.prmonth(int(Y), int(m))
else:
    Y = time.strftime('%Y')
    m = time.strftime('%m')
    calendar.prmonth(int(Y), int(m))

# EOF
