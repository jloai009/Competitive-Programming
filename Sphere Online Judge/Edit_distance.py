# https://www.spoj.com/problems/EDIST/
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A = input().rstrip()
    B = input().rstrip()
    n = len(A)
    m = len(B)
    
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(len(dp[0])):
        dp[0][i] = i
    for i in range(len(dp)):
        dp[i][0] = i
    
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = min(dp[i][j] + int(A[i]!=B[j]),
                               dp[i+1][j] + 1,
                               dp[i][j+1] + 1)
    
    
    print(dp[n][m])