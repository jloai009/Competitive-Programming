# CodeChef - FLOW010 - Id and Ship
# https://www.codechef.com/LP0TO101/problems/FLOW010

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    id_char = input().rstrip().lower()

    ship_class = None
    if id_char == 'b':
        ship_class = "BattleShip"
    elif id_char == 'c':
        ship_class = "Cruiser"
    elif id_char == 'd':
        ship_class = "Destroyer"
    elif id_char == 'f':
        ship_class = "Frigate"
    
    print(ship_class)
    