import sys; input, OUTPUT = sys.stdin.readline, []
def print(x="", end="\n"): OUTPUT.append(str(x)+end)

def main():
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        print(a*b)


if __name__ == "__main__":
    try:
        main()
        sys.stdout.write("".join(OUTPUT))
    except:
        sys.stdout.write("".join(OUTPUT))
        raise