#  Codeforces 126B Password
# https://codeforces.com/problemset/problem/126/B

import os, sys, io
sys.stdin = io.StringIO(os.read(0, os.fstat(0).st_size).decode())
input = sys.stdin.readline
DOMAIN = 26
PRIME = 2**31-1

s = input().rstrip()
n = len(s)

pows = [0]*n
pows[0] = 1

for i in range(1, len(pows)):
    pows[i] = (pows[i-1]*DOMAIN) % PRIME

hashes = [0] * (n+1)

for i in range(n):
    hashes[i+1] = (hashes[i] + (ord(s[i]) - 95) * pows[i]) % PRIME

boundaries = []

for i in range(1, n):
    suffix_hash = ( hashes[n] - hashes[n-i] + PRIME ) % PRIME
    prefix_hash = (hashes[i] * pows[n-i]) % PRIME
    if suffix_hash == prefix_hash:
        boundaries.append((i, suffix_hash))
        
def find(k, target_hash):
    for i in range(1, len(hashes)-k-1):
        hash = (hashes[i+k] - hashes[i] + PRIME) % PRIME
        hash = (hash * pows[n-(i+k)]) % PRIME
        if hash == target_hash:
            return True

    return False

low = 0
high = len(boundaries) - 1
longest_found = 0

while low <= high:
    mid = low + (high-low) // 2
    len_boundary, hash_boundary = boundaries[mid]
    if find(len_boundary, hash_boundary):
        longest_found = len_boundary
        low = mid + 1
    else:
        high = mid - 1
        

if longest_found == 0:
    print("Just a legend")
    exit(0)
    
print(s[:longest_found])