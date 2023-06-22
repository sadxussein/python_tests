from datetime import datetime

import math
import os
import random
import re
import sys

months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

def time_delta(t1, t2):
    day = t1.split()
    time = day[4].split(':')
    print(day, time)
    offset = datetime(0, 0, 0, int(day[5][1:3]), int(day[5][3:]))
    print(offset)    
    d1 = datetime(int(day[3]), int(months.get(day[2])), int(day[1], 10), int(time[0]), int(time[1]), int(time[2]))
    d1 -= offset
    print(d1)
    day = t2.split()
    print(day)

n = int(input())
for _ in range(n):
    t1 = input()
    t2 = input()
    delta = time_delta(t1, t2)