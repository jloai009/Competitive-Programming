import sys
input = sys.stdin.readline

S = set(input().rstrip())
N = int(input())
for _ in range(N):

    w = set(input().rstrip())

    if w <= S:
        print("Yes")
    else:
        print("No")
