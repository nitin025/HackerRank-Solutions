#!/bin/python3

import math
import os
import random
import re
import sys

def conditional(n):
    if n % 2 != 0:
        return 'Weird'
    else:
        if N <= 5:
            return 'Not Weird'
        elif N <= 20:
            return 'Weird'
        else:
            return 'Not Weird'

if __name__ == '__main__':
    N = int(input())
    print(conditional(N))
