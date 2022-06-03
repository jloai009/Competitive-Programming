import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    ans = (X*5 + Y*10) // Z
    print(ans)
    