import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
    
    equinox = set("EQUINOX")
    
    sarthaks_score = anuradhas_score = 0
    
    for _ in range(N):
        S = input().rstrip()
        if S[0] in equinox:
            sarthaks_score += A
        else:
            anuradhas_score += B
            
    if sarthaks_score == anuradhas_score:
        print("DRAW")
    elif sarthaks_score > anuradhas_score:
        print("SARTHAK")
    else:
        print("ANURADHA")
