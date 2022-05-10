import sys; from math import sqrt;
input = sys.stdin.readline; OUTPUT = [];  
def print(x="", end="\n"): OUTPUT.append(str(x)+end)
readInt = lambda: int(input())
readIntTuple = lambda: tuple(map(int, input().split()))
readIntList = lambda: list(map(int, input().split()))
readIntSet = lambda: set(map(int, input().split()))
mapInts = lambda: map(int, input().split())

# Code Forces 230B T-Primes
# https://codeforces.com/problemset/problem/230/B

def main():
    n = readInt()
    if n == 0:
        return
    nums = readIntTuple()
    maxNum = max(nums)

    primes = [False, False] + [True] * int(sqrt(maxNum))

    for i in range(len(primes)):
        if primes[i]:
            for j in range(i*i, len(primes), i):
                primes[j] = False

    tPrimes = set(i*i for i, b in filter(lambda x: x[1], enumerate(primes)))

    for n in nums:
        if n in tPrimes:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    try:
        main()
        sys.stdout.write("".join(OUTPUT))
    except:
        sys.stdout.write("".join(OUTPUT))
        raise