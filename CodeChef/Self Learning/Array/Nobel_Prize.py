import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = "Yes" if len(set(A)) < M else "No"
    print(ans)