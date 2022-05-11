import sys; import math; input = sys.stdin.readline
readInt = lambda: int(input())
readInts = lambda: map(int, input().split())
readStr = lambda: input().rstrip('\r\n')
readStrs = lambda: input().split()

# T9
# http://poj.org/problem?id=1451

t9 = "22233344455566677778889999"

def letterToDigits(l):
    assert 'a' <= l <= 'z'
    return t9[ord(l)-ord('a')]

def mapToDigits(word):
    return "".join(map(letterToDigits, word))


for case in range(readInt()):

    prefixWeights = {}
    w = readInt()
    for _ in range(w):
        word, weight = readStrs()
        weight = int(weight)
        prefix = ""
        for c in word:
            prefix += c
            if prefix in prefixWeights:
                prefixWeights[prefix] += weight
            else:
                prefixWeights[prefix] = weight

    masterDict = {}

    for prefix, weight in prefixWeights.items():
        digits = mapToDigits(prefix)
        if digits not in masterDict or weight > prefixWeights[masterDict[digits]]:
            masterDict[digits] = prefix

    print(f"Scenario #{case+1}:")
    m = readInt()
    for _ in range(m):
        digits = readStr()[:-1]
        prefix = ""
        for d in digits:
            prefix += d
            output = masterDict[prefix] if prefix in masterDict else "MANUALLY"
            print(output)
        print("")
    print("")
