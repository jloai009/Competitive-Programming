import collections
import sys
sys.setrecursionlimit(10000)

# Codeforces 1676G White-Black Balanced Subtrees
# https://codeforces.com/contest/1676/problem/G

for _ in range(int(input())):
    n = int(input())
    a = tuple(map(int, input().split()))
    s = input()
    
    children = collections.defaultdict(list)
    for c, p in enumerate(a, 2):
        children[p].append(c)

    res = 0

    def dp(n):
        global res
        bal = -1 if s[n-1] == "B" else 1

        for c in children[n]:
            bal += dp(c)

        if bal == 0:
            res += 1
            
        return bal
    
    dp(1)
    
    print(res)
        
    
