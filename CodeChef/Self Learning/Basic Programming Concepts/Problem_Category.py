import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x = int(input())
    if 1 <= x < 100:
        print("Easy")
    elif 100 <= x < 200:
        print("Medium")
    else:
        print("Hard")
