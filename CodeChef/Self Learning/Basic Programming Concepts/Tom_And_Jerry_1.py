import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b, c, d, K = map(int, input().split())
    dist = abs(c-a) + abs(d-b)
    if dist == K or K > dist and (K-dist) % 2 == 0:
        print("YES")
    else:
        print("NO")

