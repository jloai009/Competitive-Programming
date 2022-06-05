import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    
    P.sort(reverse=True)
    
    for p in P:
        if K % p == 0:
            print(p)
            break
    else:
        print(-1)
