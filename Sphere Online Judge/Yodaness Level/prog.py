from sys import stdin


def calculateYodaness(instance):
    """
    Yoda is the wisest, and perhaps the most powerful Jedi of his time.
    Yoda is a mysterious figure and he has many oddities.

    One of them is that Yoda often changes the order of words in the sentence.
    For example, one of such phrases is "Or I will help you not."
    Let's call the yodaness level of any statement the number of pairs of words that changed their order,
    as to the order in which they were supposed to go in a normal statement.

    Write a program that determines the yodaness level of different statement of Yoda.
    """
    n, yodaWords, originalWords = instance

    keys = {word: i for i, word in enumerate(originalWords)}

    yodaness = 0

    def mergeSort(arr):
        nonlocal yodaness

        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        pL = pR = 0

        mergeSort(L)
        mergeSort(R)

        for i in range(len(arr)):

            if pR >= len(R) or pL < len(L) and keys[L[pL]] <= keys[R[pR]]:
                yodaness += pR  # pR is the number of elements already chosen from the right subarray
                arr[i] = L[pL]
                pL += 1
            else:
                arr[i] = R[pR]
                pR += 1

        return yodaness

    print(mergeSort(yodaWords))


if __name__ == "__main__":
    """
    The first line of input contains the number t - the number of tests.
    Next comes the description of t tests. Each test consists of three rows.

    The first line of the test contains an integer n - number of words in the statement.
    The next line contains n words separated by spaces - the statement as Yoda says it.
    The next line is n words separated by spaces - the same statement as it should be said normally.

    All the words in the statement are different and consist of small latin letters.
    """

    t = int(stdin.readline())

    tests = []

    for _ in range(t):
        test = []
        test.append(int(stdin.readline()))
        test.append(stdin.readline().split())
        test.append(stdin.readline().split())
        tests.append(test)

    for test in tests:
        calculateYodaness(test)
