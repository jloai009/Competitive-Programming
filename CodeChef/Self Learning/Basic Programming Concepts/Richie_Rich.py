# CodeChef - CHFRICH - Richie Rich
# https://www.codechef.com/LP1TO201/problems/CHFRICH

import sys, math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B, X = map(int, input().split())
    ans = 0
    needed_growth = B - A
    ans = needed_growth // X
    print(ans)
