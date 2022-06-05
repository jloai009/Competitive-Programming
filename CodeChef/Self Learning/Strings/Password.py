import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = input().rstrip()
    
    has_lower = has_upper = has_digit = has_special = False
    
    specials = set("@#%&?")
    
    for i, c in enumerate(S):
        if c.islower():
            has_lower = True
        if i > 0 and i < len(S)-1:
            if c.isupper():
                has_upper = True
            if c.isdigit():
                has_digit = True
            if c in specials:
                has_special = True
    
    if has_lower and has_upper and has_digit and has_special and len(S) >= 10:
        print("YES")
    else:
        print("NO")
