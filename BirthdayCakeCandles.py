#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    count=0
    tallestcandle = max(ar)
    for i in range(len(ar)):
        if(ar[i]==tallestcandle):
            count+=1
    return count

if __name__ == '__main__':
    

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    print(result)
