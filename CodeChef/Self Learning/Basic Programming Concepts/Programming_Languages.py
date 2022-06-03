import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    A, B, A1, B1, A2, B2 = map(int, input().split())

    one = [A1, B1]
    two = [A2, B2]

    answer = 0
    if A in one and B in one:
        answer = 1
    elif A in two and B in two:
        answer = 2
    
    print(answer)