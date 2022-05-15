from itertools import accumulate, chain, permutations, combinations, combinations_with_replacement, product
from random import randint, randrange, choice,  choices, sample, shuffle, getrandbits, random
from heapq import heappush, heappop, heappushpop, heapify, nlargest, nsmallest, merge
from collections import deque, OrderedDict, Counter, defaultdict
from math import inf, sqrt, floor, ceil, factorial, gcd
from bisect import bisect_right, bisect_left, insort
from sys import stdout, setrecursionlimit
from io import BytesIO, StringIO
from functools import reduce
from os import read, fstat
from array import array

setrecursionlimit(6000)

RANDOM_MASK = getrandbits(31)
class myint(int):
    def __hash__(self):
        return self^RANDOM_MASK
int = myint

stdin = BytesIO(read(0, fstat(0).st_size))
#stdin = StringIO(read(0, fstat(0).st_size).decode())
input = stdin.readline
write = stdout.write

# SPOJ - INOUTEST - Enormous Input and Output Test
# https://www.spoj.com/problems/INOUTEST/
# 
# The purpose of this problem is to determine whether
# your method of reading input data and writing output data
# is fast enough to process extremely large test cases.

if __name__ == "__main__":
    a = input()
    N = int(a)
    for _ in range(N):
        a, b = input().split()
        write(str(int(a) * int(b)) +"\n")