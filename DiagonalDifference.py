#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diag1 =0
    diag2=0
    length = len(arr[0])
    for count in range(length):
        diag1 += arr[count][count]
        diag2 += arr[count][(length-count-1)]
    return abs(diag1-diag2)

if __name__ == '__main__':
    

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
