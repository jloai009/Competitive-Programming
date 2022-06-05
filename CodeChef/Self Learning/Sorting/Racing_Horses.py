import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    
    S.sort()
    
    answer = min(S[i]-S[i-1] for i in range(1, N))
    
    print(answer)
