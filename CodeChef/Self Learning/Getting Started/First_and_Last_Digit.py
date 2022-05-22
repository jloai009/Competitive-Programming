# CodeChef - FLOW004 - First and Last Digit
# https://www.codechef.com/LP0TO101/problems/FLOW004

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = input().rstrip()

    ans = int(N[0]) + int(N[-1])

    print(ans)