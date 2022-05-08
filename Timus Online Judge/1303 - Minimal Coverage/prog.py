from sys import stdin


def findMinimalCoverage(M, segments):
    """
    Given set of line segments [L i, R i] with integer coordinates of their end points.
    Your task is to find the minimal subset of the given set which covers segment [0, M] completely (M is a positive integer).
    """
    segments = list(filter(lambda x: not x[1] < 0 or not x[0] > M, segments))

    segments.sort()

    si = -1

    for i in range(len(segments)):
        if segments[i][0] <= 0 <= segments[i][1]:
            if si == -1 or segments[i][1] > segments[si][1]:
                si = i

    if si == -1:
        print("No solution")
        return

    minimumCoverage = [segments[si]]

    i = si+1

    while i < len(segments) and minimumCoverage[-1][1] < M:
        next = -1
        j = i
        while j < len(segments) and segments[j][0] <= minimumCoverage[-1][1]:
            if next == -1 or segments[j][1] >= segments[next][1]:
                next = j
                if segments[next][1] >= M:
                    break
            j += 1
        if next == -1:
            print("No solution")
            return
        minimumCoverage.append(segments[next])
        i = next + 1

    if minimumCoverage[-1][1] < M:
        print("No solution")
        return

    print(len(minimumCoverage))
    for segment in minimumCoverage:
        print(f"{segment[0]} {segment[1]}")


if __name__ == "__main__":
    """
    First line of the input contains an integer M (1 ≤ M ≤ 5000).
    Subsequent lines of input contain pairs of integers L i and R i (-50000 ≤ L i < R i ≤ 50000).
    Each pair of coordinates is placed on separate line.
    Numbers in the pair are separated with space.
    Last line of input data contains a pair of zeroes.
    The set contains at least one and at most 99999 segments.
    """

    M = int(stdin.readline())
    lineSegments = []
    for line in stdin:
        lineSegments.append([int(x) for x in line.split()])

    findMinimalCoverage(M, lineSegments)
