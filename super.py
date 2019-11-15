import math
import os
import random
import re
import sys

def superDigit(n, k):
    m = n * k

    while True:
        m = sum(list(map(int, m)))
        m = str(m)
        if len(m) == 1:
            return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
