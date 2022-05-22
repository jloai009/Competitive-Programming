# CodeChef - TWODISH - Two Dishes
# https://www.codechef.com/LP1TO201/problems/TWODISH

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, A, B, C = map(int, input().split())
    ans = "YES" if A+C >= N and B >= N else "NO"
    print(ans)
