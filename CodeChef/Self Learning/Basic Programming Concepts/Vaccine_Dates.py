# CodeChef - VDATES - Vaccine Dates
# https://www.codechef.com/LP1TO201/problems/VDATES

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    D, L, R = map(int, input().split())
    ans = "Too Late"
    if D <= R:
        ans = "Take second dose now"
    if D < L:
        ans = "Too Early"
    print(ans)
    