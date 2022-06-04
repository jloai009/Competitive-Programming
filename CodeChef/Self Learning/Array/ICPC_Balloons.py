import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    desk = set()
    for num_problems, balloon in enumerate(A, 1):
        if 1 <= balloon <= 7:
            desk.add(balloon)
            if len(desk) == 7:
                print(num_problems)
                break
            