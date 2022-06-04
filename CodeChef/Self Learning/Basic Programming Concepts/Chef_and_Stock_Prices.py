T = int(input())
for _ in range(T):
    S, A, B, C = map(int, input().split())
    S = S/100 *(C+100)
    if A <= S <= B:
        print("Yes")
    else:
        print("No")

