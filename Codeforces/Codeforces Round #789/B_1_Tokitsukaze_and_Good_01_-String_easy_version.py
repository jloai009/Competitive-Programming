# Codeforces 1678B1  Tokitsukaze and Good 01-String (easy version)
# https://codeforces.com/contest/1678/problem/B1

import sys
input = sys.stdin.readline
from array import array


def solve():
    n = int(input())
    s = input().rstrip()
    count = 0
    for i in range(0, len(s), 2):
        if s[i]!=s[i+1]:
            count += 1
    return count

for _ in range(int(input())):
    print(solve())