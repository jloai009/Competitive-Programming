import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    X = input().rstrip()
    Y = input().rstrip()
    
    for i in range(len(X)):
        if X[i] != Y[i] and X[i] != "?" and Y[i] != "?":
            print("No")
            break
    else:
        print("Yes")
