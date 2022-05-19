from collections import Counter
T = int(input())
for _ in range(T):
    N = int(input())
    contest_codes = input().split()
    counts = Counter(contest_codes)
    print(counts['START38'], counts['LTIME108'])