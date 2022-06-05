import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    W = list(map(int, input().split()))
    W.sort()
    

    light_sum = sum(W[:K])
    heavy_sum = sum(W[K:])
    answer = heavy_sum - light_sum
    
    light_sum2 = sum(W[:-K])
    heavy_sum2 = sum(W[-K:])
    answer = max(answer, heavy_sum2 - light_sum2)
    
    print(answer)