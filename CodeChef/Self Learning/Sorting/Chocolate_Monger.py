import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    total_chocolates, x = map(int, input().split())
    A = list(map(int, input().split()))
    
    num_types = len(set(A))
    
    repeated_chocolates = total_chocolates - num_types
    
    x -= repeated_chocolates
    
    if x <= 0:
        print(num_types)
    else:
        print(num_types - x)
