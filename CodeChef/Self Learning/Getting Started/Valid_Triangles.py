# CodeChef - FLOW013 - Valid Triangles
# https://www.codechef.com/LP0TO101/problems/FLOW013

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    ans = 'YES' if A+B+C == 180 else 'NO'
    print(ans)
