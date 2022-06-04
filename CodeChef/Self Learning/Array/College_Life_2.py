import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = int(input())
    Q = list(map(int, input().split()))
    answer = 0 
    for i in range(S):
        E = list(map(int, input().split()))
        answer += sum(E[1:]) - Q[i]*(len(E)-2)
    print(answer)
