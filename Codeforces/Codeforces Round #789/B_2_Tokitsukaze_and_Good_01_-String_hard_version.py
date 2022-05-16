# Codeforces 1678B1  Tokitsukaze and Good 01-String (hard version)
# https://codeforces.com/contest/1678/problem/B2

import sys
input = sys.stdin.readline
from array import array


def solve():
    n = int(input())
    s = list(input().rstrip())
    count = 0
    minSegs = 0
    LAST = -1
    for i in range(0, len(s), 2):
        if s[i]!=s[i+1]:
            count += 1
        else:
            minSegs +=  s[i] != LAST
            LAST = s[i]
            
    return count, max(minSegs, 1)

for _ in range(int(input())):

    print(*solve())