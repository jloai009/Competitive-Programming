import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c, x, y = map(int, input().split())
    needed_dog_food = max(0, x-a)
    needed_cat_food = max(0, y-b)
    answer = "YES" if c >= needed_cat_food + needed_dog_food else "NO"
    print(answer)
