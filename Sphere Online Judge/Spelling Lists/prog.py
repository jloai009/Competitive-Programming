from sys import stdin
from itertools import permutations


def indexInSortedPermutations(spellingList):
    """
    J, of the Men In Black,  has been learning an alien language and has has a spelling test tomorrow.
    J, however, is bored of studying the nonsensical (and often unpronounceable) words.

    Instead, he is seeing how many ways he can reorder his spelling list. 
    After making all possible permutations of word on his list,
    he sorts the rearranged lists lexicographically (by the first word, then the second...).
    After the sort, in what position, with  the lexicographically first list being in position 1, is his original spelling list?
    """

    words, n = spellingList

    nFact = n

    for i in range(n-1, 0, -1):
        nFact *= i

    idxInSortedPerm = 0

    for i, w in enumerate(words):
        wordWeights= {word: idx for idx, word in enumerate(sorted(words[i:]))}

        nFact //= len(words)-i

        idxInSortedPerm += nFact*wordWeights[w]

    print(idxInSortedPerm+1)


if __name__ == "__main__":
    T = int(stdin.readline())

    instances = []

    for _ in range(T):
        n = int(stdin.readline())
        spellingList = tuple(stdin.readline().split())
        instances.append([spellingList, n])

    for instance in instances:
        indexInSortedPermutations(instance)
