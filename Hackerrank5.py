#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if 2<= n <=20:
        for i in range(1, 11):
            mult = n * i
            print(f"{n} x {i} = {mult}")
    else:
        print("put numbers 2 to 20")
