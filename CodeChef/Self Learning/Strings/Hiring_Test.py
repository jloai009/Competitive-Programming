import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    
    answer = []
    
    for _ in range(N):
        result = input().rstrip()
        solved = result.count("F")
        partial = result.count("P")
        if solved >= X or solved == X - 1 and partial >= Y:
            answer.append("1")
        else:
            answer.append("0")
    
    print("".join(answer))
