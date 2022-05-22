# Google Kickstart Round C 2022 - New Password
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20f15

import sys
input = sys.stdin.readline

T = int(input())
for T in range(T):
    N = int(input())
    old_pass = input().strip()
    has_lower = has_upper = has_digit = has_special = False
    SPECIALS = "#@*&"

    for c in old_pass:
        has_lower |= c.islower()
        has_upper |= c.isupper()
        has_digit |= c.isdigit()
        has_special |= c in SPECIALS

    tail = ""
    if not has_lower:
        tail += 'a'
    if not has_upper:
        tail += 'A'
    if not has_special:
        tail += '&'
    if not has_digit:
        tail += '1'
    while len(old_pass) + len(tail) < 7:
        tail += '1'
    ans = old_pass + tail
    sys.stdout.write(f"Case #{T+1}: {ans}\n")
    