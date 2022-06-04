import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    score = 0

    if sum(A) == N:
        score = 100
    elif sum(A[:M]) == M:
        score = K

    
    print(score)