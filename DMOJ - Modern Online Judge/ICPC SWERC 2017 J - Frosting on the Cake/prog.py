import sys
input = sys.stdin.readline

# ICPC SWERC 2017 J - Frosting on the Cake
# https://dmoj.ca/problem/swerc17j/submit


n = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

def cat(A):
    return [sum(A[i::3]) for i in range(3)]

A = cat(A)
B = cat(B)

ans  = [0]*3
for i in range(3):
    for j in range(3):
        ans[(i+j+2)%3] += A[i]*B[j]
        
print(ans[0], ans[1], ans[2])


