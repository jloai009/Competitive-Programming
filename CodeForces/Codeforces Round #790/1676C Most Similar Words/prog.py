import sys
import math
input = sys.stdin.readline

# Codeforces 1676C Most Similar Words
# https://codeforces.com/contest/1676/problem/C

for _ in range(int(input())):
    n, m = map(int, input().split())
    str_arr = []
    
    for _ in range(n):
        str_arr.append(input()[:-1])
    
    ans = math.inf
    for i in range(n):
        for j in range(i+1, n):
            curr_diff = 0
            for k in range(m):
                curr_diff += abs(ord(str_arr[i][k])-ord(str_arr[j][k]))
            ans = min(ans, curr_diff)

    print(ans)