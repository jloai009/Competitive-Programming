# CodeChef - HS08TEST - ATM
# https://www.codechef.com/LP0TO101/problems/HS08TEST

import sys
input = sys.stdin.readline

WITHDRAWAL_CHARGE = 0.50

X, Y = input().split()
X = int(X)
Y = float(Y)

if X % 5 == 0 and Y >= X + WITHDRAWAL_CHARGE:
    Y -= X + WITHDRAWAL_CHARGE
    
print(f"{Y:.2f}")