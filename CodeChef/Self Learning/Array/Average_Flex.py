import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    answer = 0
    A.sort()
    for s in A:
        left = 0
        right = N-1
        while left <= right:
            mid = left + (right-left)//2
            if A[mid] <= s:
                left = mid + 1
            else:
                right = mid - 1
        scores_less_or_equal = left
        better_scores = N - scores_less_or_equal
        answer += better_scores < scores_less_or_equal
    print(answer)
