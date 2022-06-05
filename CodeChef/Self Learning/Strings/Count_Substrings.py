import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    S = input().rstrip()
    
    answer = 0
    ones = 0
    
    for val in S:
        if val == "1":
            ones += 1
            answer += ones

    print(answer)
