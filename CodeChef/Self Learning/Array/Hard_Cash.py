import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int , input().split())
    A = list(map(int, input().split()))
    
    print(sum(A)%K)