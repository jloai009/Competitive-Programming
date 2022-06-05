import sys
input = sys.stdin.readline

R = int(input())
for _ in range(R):
    L = int(input())
    S = input().rstrip()

    valid = True
    balance = 0

    for char in S:
        if char == "H":
            if balance == 0:
                balance += 1
            else:
                valid = False
        elif char == "T":
            if balance == 1:
                balance -= 1
            else:
                valid = False
    
    if balance != 0:
        valid = False
        
    if valid:
        print("Valid")
    else:
        print("Invalid")
