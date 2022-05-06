from collections import Counter

def printEncryption(s):
	vowels = "aeiou"
	consonants = "bcdfghjklmnpqrstvwxyz"

	string_builder = []
	counts = Counter()

	for c in s:
		k = counts[c]
		if c in vowels:
			i = vowels.index(c) + k * 5
			string_builder.append(consonants[(i % 21)])
		else:
			i = consonants.index(c) + k * 21
			string_builder.append(vowels[(i % 5)])
		counts[c] += 1
	print("".join(string_builder))



if __name__ == "__main__":
    n = int(input())
    instances = []
    for _ in range(n):
        instances.append(input())

    for s in instances:
        printEncryption(s)
