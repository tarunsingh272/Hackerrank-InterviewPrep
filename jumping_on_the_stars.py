#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    start = 0
    end = len(c) - 1
    jumps = 0
    while start < end:
        if ((start + 2) <= end) and (c[start + 2] == 0):
            start += 2
            jumps += 1
        elif c[start + 1] == 0:
            start += 1
            jumps += 1

    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
