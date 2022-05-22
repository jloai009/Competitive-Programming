# CodeChef - HOOPS - Hoop Jump
# https://www.codechef.com/LP1TO201/problems/HOOPS

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    ans = N // 2 + 1
    print(ans)
