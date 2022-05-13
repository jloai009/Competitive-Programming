#  SPOJ - NHAY - A Needle in the Haystack
#  https://www.spoj.com/problems/NHAY/

def maximal_boudaries(w):
    k = 0
    n = len(w)
    f = [0]*n
    for i in range(1, n):
        while k > 0 and w[k] != w[i]:
            k = f[k-1]
        if w[k] == w[i]:
            k += 1
        f[i] = k
        
    return f

def solve(params):
    l, t, s = params
    f = maximal_boudaries(t+"\x00"+s)
    ans = []
    for i, n in enumerate(f):
        if n == len(t):
            ans.append(i-2*len(t))
    print(*ans, sep="\n")

def main():
    params = []
    for line in sys.stdin:
        params.append(line.rstrip())
        if len(params) == 3:
            solve(params)
            params = []

























import os, sys; from io import BytesIO, IOBase; 
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file): self._fd = file.fileno(); self.buffer = BytesIO(); self.writable = "x" in file.mode or "r" not in file.mode; self.write = self.buffer.write if self.writable else None; self.BUFSIZE = 8192
    def readline(self):
        while self.newlines == 0: b = os.read(self._fd, max(os.fstat(self._fd).st_size, self.BUFSIZE)); self.newlines = b.count(b"\n") + (not b); ptr = self.buffer.tell(); self.buffer.seek(0, 2); self.buffer.write(b); self.buffer.seek(ptr)
        self.newlines -= 1; return self.buffer.readline()
class IOWrapper(IOBase):
    def __init__(self, file): self.buffer = FastIO(file); self.flush = self.buffer.flush; self.writable = self.buffer.writable; self.write = lambda s: self.buffer.write(s.encode("ascii")); self.read = lambda: self.buffer.read().decode("ascii"); self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin = IOWrapper(sys.stdin)
def input(): return sys.stdin.readline().rstrip()

from math import *
from random import *
from collections import *
from bisect import *
from heapq import *

___ = getrandbits(31)
class myint(int):
    def __hash__(self):
        return self^___
int = myint

sys.setrecursionlimit(6000)

if __name__ == "__main__":
    main()
