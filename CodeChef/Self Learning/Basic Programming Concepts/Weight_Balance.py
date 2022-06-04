T = int(input())
for _ in range(T):
    w1, w2, x1, x2, M = map(int, input().split())
    weight_gain = w2 - w1

    ans = x1*M <= weight_gain <= x2*M

    print(int(ans)) 
    
