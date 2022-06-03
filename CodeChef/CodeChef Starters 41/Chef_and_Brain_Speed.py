import sys
input = sys.stdin.readline

X, Y = map(int, input().split())

print("YES" if Y > X else "NO")
