import sys; import math; input = sys.stdin.readline
readInt = lambda: int(input())
readInts = lambda: map(int, input().split())
readStr = lambda: input().rstrip('\r\n')
readStrs = lambda: input().split()

# CodeForces 1676D X-Sum

for t in range(readInt()):
    n, m = readInts()
    a = []
    f = [0]*(n+m)
    g = [0]*(n+m)
    for i in range(n):
        a.append(tuple(readInts()))
        for j in range(m):
            f[i+j] += a[i][j]
            g[i-j+m] += a[i][j]

    print(max(f[i+j]+g[i-j+m]-a[i][j] for j in range(m) for i in range(n)))
