import sys

from heapq import nsmallest

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    answer = sum(nsmallest(2, A))

    print(answer)