#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair_dict = {}
    for color in ar:
        pair_dict[color] = pair_dict.get(color,0) + 1
        
    count_of_pairs = 0
    for key, values in pair_dict.items():
        count_of_pairs = count_of_pairs + (values // 2)
    return count_of_pairs
   


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
