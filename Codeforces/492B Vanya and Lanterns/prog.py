import sys; input = sys.stdin.readline; OUTPUT = [];  
def print(x="", end="\n"): OUTPUT.append(str(x)+end)
readInt = lambda: int(input())
readIntTuple = lambda: tuple(map(int, input().split()))
readIntList = lambda: list(map(int, input().split()))
readIntSet = lambda: set(map(int, input().split()))
mapInts = lambda: map(int, input().split())

# Code Forces 492B Vanya and Lanterns
# https://codeforces.com/problemset/problem/492/B

def main():
    n, l = mapInts()
    lanterns = readIntList()
    lanterns.sort()
    distToZero = lanterns[0]
    distToEnd = l-lanterns[-1]
    maxDistBetLants = 0
    for i in range(len(lanterns)-1):
        maxDistBetLants = max(maxDistBetLants, lanterns[i+1]-lanterns[i])
    d = max(distToZero, distToEnd, maxDistBetLants/2)
    print(f"{d:.10f}")
    


if __name__ == "__main__":
    try:
        main()
        sys.stdout.write("".join(OUTPUT))
    except:
        sys.stdout.write("".join(OUTPUT))
        raise