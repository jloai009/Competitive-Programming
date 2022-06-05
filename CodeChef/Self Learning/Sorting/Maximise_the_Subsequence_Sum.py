import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))


    positives = [n for n in A if n > 0]
    negatives = [-n for n in A if n < 0]

    negatives.sort(reverse = True)

    answer = sum(positives) + sum(negatives[:K])


    print(answer)
