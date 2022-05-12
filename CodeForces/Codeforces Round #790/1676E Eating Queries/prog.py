import sys
import math
import itertools
import bisect
input = sys.stdin.readline

# Codeforces 1676E Eating Queries
# https://codeforces.com/contest/1676/problem/E

for _ in range(int(input())):
    n, q = map(int, input().split())
    candies = list(map(int, input().split()))
    candies.sort(reverse=True)
    candies = list(itertools.accumulate(candies))
    for _ in range(q):
        x = int(input())
        num = -1
        left = 0
        right = n-1
        while left <= right:
            mid = left + (right-left)//2
            if candies[mid] >= x:
                num = mid
                right = mid - 1
            else:
                left = mid + 1
        print(num+1 if num != -1 else -1)
        
    
    
    