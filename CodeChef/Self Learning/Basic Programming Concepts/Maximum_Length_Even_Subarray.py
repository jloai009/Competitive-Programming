T = int(input())
for _ in range(T):
    N = int(input())
    total = N(N+1)//2
    if total % 2 == 0:
        print(N)
    else:
        print(N-1)
