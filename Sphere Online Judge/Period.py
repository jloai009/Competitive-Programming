
#  SPOJ - PERIOD - Period
#  https://www.spoj.com/problems/PERIOD/

def maximal_boundaries(w):
    n = len(w)
    f = array('i', [0]) * n
    k = 0
    for i in range(1, n):
        while k > 0 and w[k]!=w[i]:
            k = f[k-1]
        k += w[i]==w[k]
        f[i] = k
    return f

def solve(case):
    N = int(input())
    S = input()
    f = maximal_boundaries(S)

    print(f"Test case #{case}")

    for i in range(1, len(S)):

        substr_length = i+1
        boundary_length = f[i]

        alignment_shift = substr_length - boundary_length 
        if boundary_length != 0 and substr_length % alignment_shift == 0:
            print(substr_length, substr_length // alignment_shift)

    print()

def main():
    for case in range(1, int(input())+1):
        solve(case)






































import os
import sys
from io import BytesIO, IOBase
from math import *
from random import *
from collections import *
from bisect import *
from heapq import *
from array import array

class FastInput(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.BUFSIZE = 8192

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, self.BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline().decode("ascii").rstrip()

sys.stdin = FastInput(sys.stdin)
input = sys.stdin.readline

RANDOM_MASK = getrandbits(31)
class myint(int):
    def __hash__(self):
        return self^RANDOM_MASK
int = myint

sys.setrecursionlimit(6000)

if __name__ == "__main__":
    main()
