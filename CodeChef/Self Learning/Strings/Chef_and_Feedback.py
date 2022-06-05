import sys
input = sys.stdin.readline

def maximal_boundaries(w):
    f = [0] * len(w)
    k = 0
    for i in range(1, len(w)):
        while k > 0 and w[k] != w[i]:
            k = f[k-1]
        k += w[k] == w[i]
        f[i] = k
    return f

T = int(input())

for _ in range(T):
    S = input().rstrip()

    answer = "Bad"
    
    kmp_string = "010" + "#" + S
    if 3 in maximal_boundaries(kmp_string):
        answer = "Good"

    kmp_string2 = "101" + "#" + S
    if 3 in maximal_boundaries(kmp_string2):
        answer = "Good"

    print(answer)
