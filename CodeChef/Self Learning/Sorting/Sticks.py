import sys, collections
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    A.sort(reverse=True)
    
    ans = 1
    pairs_found = 0
    
    i = 0
    while i < N - 1:
        if A[i] == A[i+1]:
            pairs_found += 1
            ans *= A[i]
            i += 1
            if pairs_found == 2:
                break
        i += 1
        
    if pairs_found == 2:
        print(ans)
    else:
        print(-1)
