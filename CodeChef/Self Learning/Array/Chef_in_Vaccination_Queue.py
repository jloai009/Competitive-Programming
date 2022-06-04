import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, P, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    answer = 0
    for i in range(P):
        if A[i]:
            answer += Y
        else:
            answer += X

    print(answer)

