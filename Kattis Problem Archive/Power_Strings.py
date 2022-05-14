#  Kattis - Power Strings
#  https://open.kattis.com/problems/powerstrings


def main():
    while True:
        w = input()
        if w == ".":
            break
        n = len(w)
        f = array("i", [0])*n
        k = 0
        for i in range(1, n):
            while k and w[k] != w[i]:
                k = f[k-1]

            k += (w[k]==w[i])
            f[i] = k

        if n % (n-f[-1]) == 0:
            print(n // (n-f[-1]))
        else:
            print(1)
    






























import os
from sys import stdin, setrecursionlimit
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
        self.newlines -= 1;
        return self.buffer.readline().decode("ascii").rstrip()

stdin = FastInput(stdin)
input = stdin.readline

RANDOM_MASK = getrandbits(31)
class myint(int):
    def __hash__(self):
        return self^RANDOM_MASK
int = myint

setrecursionlimit(6000)

if __name__ == "__main__":
    main()
