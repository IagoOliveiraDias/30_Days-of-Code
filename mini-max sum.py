#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
        soma = 0
        soma = sum(arr)
        minus = sum(arr) - max(arr)
        maximus = sum(arr) - min(arr)

        print(f"{minus} {maximus}")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
