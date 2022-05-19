T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    points_A = 500 - X*2
    points_B = 1000 - Y*4
    print( max(points_A + points_B - X*4, points_B + points_A - Y*2 ) )