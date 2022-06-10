from sys import stdin
from collections import Counter

input = stdin.readline

M, N = map(int, input().split())
A = []
for _ in range(M):
    A.append(list(map(int, input().split())))

for i in range(M):
    for j in range(1, N):
        A[i][j] += A[i][j-1]

for i in range(1, M):
    for j in range(N):
        A[i][j] += A[i-1][j]

C = int(input())
for _ in range(C):
    x1, y1, x2, y2 = map(int, input().split())
    
    x1, y1 = x1-1, y1-1
    x2, y2 = x2-1, y2-1
    
    total = A[x2][y2]

    if x1 > 0 and y1 > 0:
        total += A[x1-1][y1-1]

    if y1 > 0:
        total -= A[x2][y1-1]

    if x1 > 0:
        total -= A[x1-1][y2]

    print(total)
