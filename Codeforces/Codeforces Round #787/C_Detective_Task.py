import sys 
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().rstrip()
    suspects = 0

    first_zero = s.find('0')
    if first_zero != -1:
        suspects += 1
    else:
        first_zero = len(s)

    last_one = -1
    for i in range(len(s)-1, -1, -1):
        if s[i] == '1':
            last_one = i
            suspects += 1
            break

    suspects += first_zero - last_one - 1

    print(suspects)