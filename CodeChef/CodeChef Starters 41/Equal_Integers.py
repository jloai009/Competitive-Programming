import sys, math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    ops = 0
    
    if X < Y:
        ops = Y - X
        
    if X > Y:
        diff = X - Y
        ops = math.ceil(diff/2) + (diff&1)
       
    print(ops)