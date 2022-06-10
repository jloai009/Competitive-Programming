from sys import stdin
from collections import Counter

input = stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))

    max_sum = float("-inf")
    curr_sum = 0

    for num in A:
        curr_sum = max(curr_sum+num, num)
        max_sum = max(max_sum, curr_sum)

    answer = 0
    h = Counter()
    running_sum = 0

    for num in A:
        running_sum += num
        if running_sum == max_sum:
            answer += 1
        answer += h[running_sum-max_sum]

        h[running_sum] += 1

    print (max_sum, answer)
