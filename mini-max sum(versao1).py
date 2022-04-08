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
    minimo = 0
    maximo = 0
    soma = 0
    minimo = arr[0]
    maximo = minimo
    minimo = maximo

    for i in range (len(arr)):
        soma += arr[i]
        if arr[i] < minimo:
            minimo = arr[i]
        elif arr[i]>maximo :
            maximo = arr[i]
    print(str(soma - maximo) + " " + str(soma - minimo))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
