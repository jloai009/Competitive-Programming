import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, x, y = map(int, input().split())
    house_nums = list(map(int, input().split()))
    search_radius = x * y
    good_houses = [False] + [True]*100
    for h in house_nums:
        for i in range(max(0, h-search_radius), min(h+search_radius+1, len(good_houses))):
            good_houses[i] = False
    
    answer = sum(good_houses)
    print(answer)
