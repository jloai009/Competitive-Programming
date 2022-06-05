import sys
input = sys.stdin.readline

N, D = map(int, input().split())
L = []
for _ in range(N):
    L.append(int(input()))
    
L.sort()

pairs = 0

i= 0
while i < (N - 1):
    if L[i+1]-L[i] <= D:
        pairs += 1
        i += 1
    i += 1

print(pairs)