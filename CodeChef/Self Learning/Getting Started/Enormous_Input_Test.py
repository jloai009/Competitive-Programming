# CodeChef - INTEST - Enormous Input Test
# https://www.codechef.com/LP0TO101/problems/INTEST

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ans = 0
for _ in range(n):
    t = int(input())
    ans += t % k == 0
    
print(ans)