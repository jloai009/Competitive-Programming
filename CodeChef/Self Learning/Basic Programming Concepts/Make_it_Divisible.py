import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    
    a =  '1' + '0' * (N-1)
    
    a = int(a)
    
    while True:
        if a % 3 == 0 and a % 2 != 0 and a % 9 != 0:
        
            print(a)
            break
            
        a += 1
