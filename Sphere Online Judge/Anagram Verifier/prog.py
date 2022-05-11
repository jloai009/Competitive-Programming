import sys; import math; input = sys.stdin.readline
from collections import Counter
readInt = lambda: int(input())
readInts = lambda: map(int, input().split())
readStr = lambda: input().rstrip('\r\n')
readStrs = lambda: input().split()

# SPOJ - ANGRAM - Anagram verifier
# https://www.spoj.com/problems/ANGRAM/

for T in range(readInt()):
    s1, s2 = readStrs()
    if Counter(s1) == Counter(s2):
        print("true")
    else:
        print("false")
