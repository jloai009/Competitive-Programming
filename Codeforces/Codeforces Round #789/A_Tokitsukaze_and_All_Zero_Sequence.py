
# Codeforces 1678A Tokitsukaze and All Zero Sequence
# https://codeforces.com/contest/1678/problem/A

# Tokitsukaze has a sequence a of length n.
# For each operation, she selects two numbers ai and aj (i≠j; 1≤i,j≤n).

#     If ai=aj, change one of them to 0.
#     Otherwise change both of them to min(ai,aj). 

# Tokitsukaze wants to know the minimum number of operations to change all numbers in the sequence to 0.
# It can be proved that the answer always exists.


import sys
from array import array
from collections import Counter
input = sys.stdin.readline


def solve():
    n = int(input())
    a = array("i", map(int, input().split()))
    h = Counter(a)
    if 0 in h:
        return n - h[0]
    
    for num, count in h.items():
        if count >=  2:
            return n
    
    return n + 1


for _ in range(int(input())):
    print(solve())