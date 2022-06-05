import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

b = [float("-inf")]

for i in range(len(A)):
    if A[i] > b[-1]:
        b.append(A[i])
    else:
        k = bisect_left(b, A[i])
        b[k] = A[i]

print(len(b)-1)