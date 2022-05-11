import sys; import math; input = sys.stdin.readline
readInt = lambda: int(input())
readInts = lambda: map(int, input().split())
readStr = lambda: input().rstrip('\r\n')
readStrs = lambda: input().split()

# CodeForces 474B Worms
# https://codeforces.com/problemset/problem/474/B

n = readInt()
w = tuple(readInts())
m = readInt()
l = tuple(readInts())
p = [0]
for n in w:
    p.append(p[-1]+n)

for q in l:
    left = 0
    right = len(p)-1
    
    while left <= right:
        mid = left + (right-left)//2
        if p[mid] == q:
            print(mid)
            break
        elif p[mid] < q:
            left = mid + 1
        else:
            right = mid - 1
    else:
        print(left)
