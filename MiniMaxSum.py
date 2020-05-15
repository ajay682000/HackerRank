#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    x=0
    for i in range(len(arr)):
        x+=arr[i]
    a=(x-max(arr))
    b=(x-min(arr))
    print(a,b)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
