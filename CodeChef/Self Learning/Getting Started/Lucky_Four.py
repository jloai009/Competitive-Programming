# CodeChef - LUCKFOUR - Lucky Four
# https://www.codechef.com/LP0TO101/problems/LUCKFOUR

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = input().rstrip()
    ans = N.count('4')
    print(ans)
