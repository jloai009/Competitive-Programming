import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    S = "1" + input().rstrip()
    answer = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            answer += 1
            
    print(answer)