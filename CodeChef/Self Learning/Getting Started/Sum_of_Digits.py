import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = input().rstrip()
    ans = sum(int(c) for c in N)
    print(ans)
