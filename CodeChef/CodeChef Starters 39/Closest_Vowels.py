# CodeChef CLOSEVOWEL Closest Vowels
# https://www.codechef.com/problems/CLOSEVOWEL

import sys
input = sys.stdin.readline
MOD = 1000000007

T = int(input())

for _ in range(T):
    N = int(input())
    S = input().rstrip()

    ans = 1

    s = set("cglr")
    for c in S:
        if c in s:
            ans = (ans * 2) % MOD

    print(ans)