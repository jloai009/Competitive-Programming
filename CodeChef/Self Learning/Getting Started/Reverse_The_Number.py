import sys
input  = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = input().rstrip()
    ans = N[::-1].lstrip("0")
    print(ans)