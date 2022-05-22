# CodeChef - IMDB - Motivation
# https://www.codechef.com/LP1TO201/problems/IMDB


import sys, math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    highest_rating = -math.inf

    for _ in range(N):
        S, R = map(int, input().split())
        if S <= X:
            highest_rating = max(highest_rating, R)
    
    print(highest_rating)
