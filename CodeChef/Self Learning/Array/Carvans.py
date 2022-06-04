# https://www.codechef.com/LP1TO202/problems/CARVANS

import sys, math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    speeds = list(map(int, input().split()))
    
    min_speed = math.inf
    
    ans = 0
    
    for s in speeds:
        if s <= min_speed:
            ans += 1
            min_speed = min(min_speed, s)
            
    print(ans)