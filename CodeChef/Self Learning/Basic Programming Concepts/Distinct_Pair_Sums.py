T = int(input())
for _ in range(T):
    L, R = map(int, input().split())
    print(R*2-L*2+1)
