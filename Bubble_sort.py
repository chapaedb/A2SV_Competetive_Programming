#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    n = len(a)
    count = 0
    
    
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count += 1
                
    
    
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[n-1]}")
        

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
