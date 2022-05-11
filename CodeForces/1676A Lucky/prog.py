import sys; import math; input = sys.stdin.readline
readInt = lambda: int(input())
readInts = lambda: map(int, input().split())
readStr = lambda: input().rstrip('\r\n')
readStrs = lambda: input().split()

# CodeForces 1676A Lucky

for t in range(readInt()):
    s = readStr()
    
    if sum(map(int, s[:3])) == sum(map(int, s[-3:])):
        print("YES")
    else:
        print("NO")