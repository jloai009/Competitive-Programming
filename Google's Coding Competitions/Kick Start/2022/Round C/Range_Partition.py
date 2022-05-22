# Google Kickstart Round C 2022 - Range Partition
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20deb

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
for T in range(T):
    N, X, Y = map(int, input().split())
    total_sum = N*(N+1)//2
    if total_sum % (X+Y) != 0:
        print(f"Case #{T+1}: IMPOSSIBLE")
        continue
    answer = []
    target = X * total_sum // (X+Y)
    curr_sum = 0
    for i in range(N, 0, -1):
        if curr_sum + i <= target:
            curr_sum += i
            answer.append(i)
        if curr_sum == target:
            break
    answer.reverse()
    sys.stdout.write(f"Case #{T+1}: POSSIBLE\n{len(answer)}\n")
    print(*answer)
    