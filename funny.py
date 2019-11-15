import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def Funny(word):
    i = 0
    length = len(word)
    a = []
    b = []
    for i in range(0,math.ceil(length/2)):
        z = abs(ord(word[i])-ord(word[i+1]))
        x = abs(ord(word[length-i-1])-ord(word[length-i-2]))
        if z == x:
               continue
        else:
               return False
    return True

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        word = input();
        if Funny(word):
            print("Funny")
        else:
            print("Not Funny")
