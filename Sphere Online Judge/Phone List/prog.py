from sys import stdin
from collections import defaultdict
from functools import reduce

def isConsistent(numbers):
    """
    Given a list of phone numbers, determine if it is consistent
    in the sense that no number is the prefix of another
    """
    trie = {}
    ENDWORD = True

    numbers.sort(key=len)

    for num in numbers:
        pT = trie

        for c in num:
            if c not in pT:
                pT[c] = {}
            pT = pT[c]
            if ENDWORD in pT:
                return "NO"

        pT[ENDWORD] = num

    return "YES"


if __name__ == "__main__":
    t = int(stdin.readline())
    instances = []
    for _ in range(t):
        n = int(stdin.readline())
        current_instance = []
        for _ in range(n):
            current_instance.append(stdin.readline()[:-1])
        instances.append(current_instance)

    for numbers in instances:
        print(isConsistent(numbers))