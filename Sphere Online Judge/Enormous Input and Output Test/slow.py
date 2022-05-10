import sys; input = sys.stdin.readline;
def print(x="", end="\n"): sys.stdout.write(str(x)+end)

def main():
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        print(a*b)


if __name__ == "__main__":
    main()