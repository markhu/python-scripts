#!/usr/bin/env python

# cal.py
# emulate the original Unix `cal` command

# TBD: highlight the current day (cross-platform Linux + Windows)

import sys

import calendar
import time   # simpler than datetime

calendar.setfirstweekday(calendar.SUNDAY)

def cal_y(Y):
    calendar.prcal(int(Y))

def cal(m, Y):
    calendar.prmonth(int(Y), int(m))

def test_cal():
    print ""
    Y = time.strftime('%Y')
    m = time.strftime('%m')
    cal(m,Y)
    pass

if __name__ == "__main__":
    if len(sys.argv) == 2:
        Y = sys.argv[1]
        cal_y(Y)
    elif len(sys.argv) == 3:
        m = sys.argv[1]
        Y = sys.argv[2]
        cal(m,Y)
    else:
        Y = time.strftime('%Y')
        m = time.strftime('%m')
        cal(m,Y)

# EOF
