import sys;
import math;
input = sys.stdin.readline

# Codeforces 1676B Equal Candies
# https://codeforces.com/contest/1676/problem/B

for _ in range(int(input())):
    n = int(input())
    candies = list(map(int, input().split()))
    print(sum(candies)-min(candies)*n)