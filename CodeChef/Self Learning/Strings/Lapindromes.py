import sys
input = sys.stdin.readline

from collections import Counter

T = int(input())
for _ in range(T):
    
    
    S = input().rstrip()
    
    mid = len(S)//2

    if len(S) % 2 != 0:
        S = S[:mid] + S[mid+1:]

    first_half = Counter(S[:mid])
    second_half = Counter(S[mid:])
    
    answer = "YES" if first_half == second_half else "NO"
    
    print(answer)
