import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    K = int(input())
    
    for i in range(len(A)-1, -1, -1):
        num_to_delete = min(A[i], K)
        A[i] -= num_to_delete
        K -= num_to_delete
        
        if K == 0 and A[i] > 0:
            print(i+1)
            break
            