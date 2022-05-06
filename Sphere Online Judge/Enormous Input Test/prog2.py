import os

if __name__ == "__main__":
    n, k = map(int, input().split())
    ints = [int(n) for n in os.read(0, 12*10**7).split()]
    count = 0

    for n in ints:
        if n % k == 0:
            count += 1

    print(count)
