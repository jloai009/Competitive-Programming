T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(N % K if K else N)
