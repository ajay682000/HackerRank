#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    p1=0
    p2=0
    for i in range(3):
        if(a[i]>b[i]):
            p1+=1
        elif(a[i]<b[i]):
            p2+=1
    return (p1, p2)

if __name__ == '__main__':
   

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

   print(result)