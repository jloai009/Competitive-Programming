from sys import stdin

if __name__ == "__main__":
	n, k = map(int, stdin.readline().split())
	count = 0
	for _ in range(n):
		if int(stdin.readline()) % k == 0:
			count += 1
	print(count)
