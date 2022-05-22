# CodeChef - MAX_DIFF - The Two Dishes
# https://www.codechef.com/LP1TO201/problems/MAX_DIFF

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, S = map(int, input().split())
    ans = S if N >= S else N-(S-N)
    print(ans)
