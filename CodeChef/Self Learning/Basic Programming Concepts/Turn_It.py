import math

T = int(input())
for _ in range(T):
    U, V, A, S = map(int, input().split())
    v = math.sqrt(max(U**2 - 2 * A * S, 0))
    if v <= V:
        print("Yes")
    else:
        print("No")

