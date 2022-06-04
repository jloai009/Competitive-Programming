T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    print(A+B+C - min(A, B, C))
