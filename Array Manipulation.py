#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    Arr = [0 for i in range(n+1)]
    for i in queries:
        Arr[i[0]-1] += i[2]
        Arr[i[1]] -= i[2]
    max = 0
    s =0
    for i in Arr:
        s += i
        if s > max:
            max = s
    return max
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
