from sys import stdin


def maxOverlappingIntervals(intervals):
    """
    Several years have passed, and alas! you can no longer participate in Prologin.
    Luckily, your DeLorean allows you to go back in time,
    and so you've decided that every year you'll relive the Prologin Finals of your choice.
    A question nags you nevertheless:
    what will be the greatest number of simultaneous occurrences of yourself?

    You are given as input the time intervals during which you will go for a ride in the past,
    and you must return the maximum number of copies of yourself having attended the same final.
    """

    sweepLine = [(a, -1, 1) for a, b in intervals]+[(b, 1, -1)
                                                    for a, b in intervals]
    sweepLine.sort()
    maxOverlap = 0
    curOverlap = 0

    for _, _, startOrEnd in sweepLine:
        curOverlap += startOrEnd
        maxOverlap = max(maxOverlap, curOverlap)

    print(maxOverlap)


if __name__ == "__main__":
    """
    On the first line, the number N of time intervals.
    On the next N lines, a pair of integers (D i , F i )
    representing the time interval (start, end)
    during which you will exist once again in the past.
    """

    N = int(stdin.readline())
    intervals = []
    for _ in range(N):
        intervals.append([int(x) for x in stdin.readline().split()])

    maxOverlappingIntervals(intervals)
