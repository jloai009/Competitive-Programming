import sys; input, OUTPUT = sys.stdin.readline, []
def print(x="", end="\n"): OUTPUT.append(str(x)+end)
readInt = lambda: int(input())
mapInts = lambda: map(int, input().split())

# Code Forces 750A New Year and Hurry
# https://codeforces.com/problemset/problem/750/A

def main():
    n, k = mapInts()
    end = 240 - k
    i = 1
    while i <= n and end - 5*i >= 0:
        end -= 5*i
        i += 1 
    print(i-1)

if __name__ == "__main__":
    try:
        main()
        sys.stdout.write("".join(OUTPUT))
    except:
        sys.stdout.write("".join(OUTPUT))
        raise