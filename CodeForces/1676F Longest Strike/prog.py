from collections import Counter
import math

# Codeforces 1676F Longest Strike
# https://codeforces.com/contest/1676/problem/F

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    h = Counter(a)
    ans = (-math.inf, -1, -1)
    left = 0
    for right in range(n):
        if h[a[right]] < k:
            left = right + 1
            continue
        if right != 0 and a[right]-a[right-1] > 1 and right != left:
            left = right
            continue
        if a[right] - a[left] > ans[0]:
            ans = (a[right] - a[left], left, right)
            
    if ans[1]== -1 or ans[2] == -1:
        print(-1)
    else:
        print(f"{a[ans[1]]} {a[ans[2]]}")