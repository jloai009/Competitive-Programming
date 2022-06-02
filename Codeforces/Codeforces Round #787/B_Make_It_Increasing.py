import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    ops = 0
    for i in range(len(nums)-2, -1, -1):
        if nums[i+1] == 0:
            ops = -1
            break
        while nums[i] >= nums[i+1]:
            nums[i] //= 2
            ops += 1
    print(ops)