import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
T = []

ans = 0

for _ in range(N):
    student_info = list(map(int, input().split()))

    ans += sum(student_info[:-1]) >= M and student_info[-1] < 11


print(ans)
