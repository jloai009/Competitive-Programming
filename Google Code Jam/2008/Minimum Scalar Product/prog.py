from sys import stdin


def minimumScalarProduct(vectors, case):
    """
    You are given two vectors v1 = (x1, x2, ..., xn) and v2 = (y1, y2, ..., yn).
    The scalar product of these vectors is a single number, calculated as x1y1 + x2y2 + ... + xnyn.

    Suppose you are allowed to permute the coordinates of each vector as you wish.
    Choose two permutations such that the scalar product of your two new vectors is the smallest possible,
    and output that minimum scalar product.

    """
    v1, v2 = vectors
    v1 = sorted(v1)
    v2 = sorted(v2)

    minScaProd = sum(v1[i]*v2[~i] for i in range(len(v1)))

    print(f"Case #{case}: {minScaProd}")


if __name__ == "__main__":
    T = int(stdin.readline())

    instances = []

    for _ in range(T):
        n = int(stdin.readline())
        vectors = []
        vectors.append([int(x) for x in stdin.readline().split()])
        vectors.append([int(x) for x in stdin.readline().split()])
        instances.append(vectors)

    for i, vectors in enumerate(instances):
        minimumScalarProduct(vectors, i+1)
