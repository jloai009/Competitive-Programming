import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

n = len(A)
m = len(B)


dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

answer = 0
for i in range(n):
    for j in range(m):
        if A[i] == B[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        answer = max(answer, dp[i+1][j+1])


print(answer)
