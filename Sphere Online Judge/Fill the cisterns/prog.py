import sys; input, OUTPUT = sys.stdin.readline, []
def print(x="", end="\n"):
    OUTPUT.append(str(x)+end)
readInt = lambda: int(input())
mapInts = lambda: map(int, input().split())

# SPOJ - CISTFILL - Fill the Cisterns
# https://www.spoj.com/problems/CISTFILL/


def computeWaterLevel(dataset):
    cisterns, V = dataset

    maxLevel = max(cistern[0]+cistern[1] for cistern in cisterns)

    def getVolume(level):
        V = 0
        for cist in cisterns:
            V += cist[2] * min(cist[1], max(level-cist[0], 0))
        return V

    if getVolume(maxLevel) < V:
        print("OVERFLOW")
        return

    low = 0
    high = maxLevel

    while high-low > 0.0001:
        mid = (low+high)/2
        if getVolume(mid) >= V:
            high = mid
        else:
            low = mid

    print(f"{low:.2f}")


def main():
    k = readInt()
    datasets = []
    for _ in range(k):
        n = readInt()
        
        cisterns = []
        for _ in range(n):
            b, h, w, d = mapInts()
            cisterns.append((b, h, w*d))

        V = readInt()
        datasets.append((cisterns, V))

    for data in datasets:
        computeWaterLevel(data)










if __name__ == "__main__":
    try:
        main()
        sys.stdout.write("".join(OUTPUT))
    except:
        sys.stdout.write("".join(OUTPUT))
        raise