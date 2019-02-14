#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level = 0
    up = 0
    down = 0
    valley = 0
    mountains = 0
    
    for char in s:
        if char == 'U':
            sea_level += 1
            if sea_level==0:
                valley +=1
        else:
            sea_level -=1
            
    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
