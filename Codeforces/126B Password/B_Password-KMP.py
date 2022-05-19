#  Codeforces 126B Password
# https://codeforces.com/problemset/problem/126/B

import os, sys, io, array
sys.stdin = io.StringIO(os.read(0, os.fstat(0).st_size).decode())
input = sys.stdin.readline

s = input().rstrip()

LPS = array.array('i', [0])* len(s)
k = 0

for i in range(1, len(s)):
    while s[i] != s[k] and k:
        k = LPS[k-1]
        
    k += s[i] == s[k]
    
    LPS[i] = k
    
len_boundary = LPS[-1]

if len_boundary == 0:
    print("Just a legend")
    exit(0)
    
for n in LPS[:-1]:
    if n == len_boundary:
        print(s[:len_boundary])
        exit(0)

if LPS[len_boundary-1] == 0:
    print("Just a legend")
    exit(0)

print(s[:LPS[len_boundary-1]])