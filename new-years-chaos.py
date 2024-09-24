#!/bin/python3

import math
import os
import random
import re
import sys

def minimumBribes(q):
    bribe = 0
    min1 = sys.maxsize
    min2 = sys.maxsize

    for i in reversed(range(len(q))):
        val = q[i]

        if val-i-1 > 2:
            print("Too chaotic")
            return
        
        if val > min1:
            bribe += 1
        if val > min2:
            bribe += 1

        if val < min1:
            min2 = min1
            min1 = val
        elif val < min2:
            min2 = val

    print(bribe)
if __name__ == '__main__':
    q = [5,1,2,3,7,8,6,4]
    q2 = [1,2,5,3,7,8,6,4]

    minimumBribes(q)
    minimumBribes(q2)