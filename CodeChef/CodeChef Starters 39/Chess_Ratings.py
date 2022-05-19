import math
T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    needed_rating = Y - X
    needed_games = math.ceil(needed_rating / 8)
    print(needed_games)