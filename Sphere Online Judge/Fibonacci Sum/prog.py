from sys import stdin


def fibonacciSums(tests):
    """
    The fibonacci sequence is defined by the following relation:
    F(0) = 0
    F(1) = 1
    F(N) = F(N - 1) + F(N - 2), N >= 2

    Your task is very simple. Given two non-negative integers N and M,
    you have to calculate the sum (F(N) + F(N + 1) + ... + F(M)) mod 1000000007.
    """

    mod = 1000000007

    # the sum of the first n fibonacci numbers is fib(n+2)-1
    for low, high in tests:
        lowSum = (fibMod(low+1, mod)-1+mod) % mod
        highSum = (fibMod(high+2, mod)-1+mod) % mod
        fibSum = (highSum - lowSum + mod) % mod
        print(fibSum)


def fibMod(n, mod):
    if n <= 1:
        return n

    fibQMatrix = [[1, 1],
                  [1, 0]]

    def matrixPow(A, n):
        if n <= 1:
            return A
        matrixPow(A, n//2)
        mult(A, A)

        if n % 2 != 0:
            mult(A, fibQMatrix)

    def mult(A, B):
        x = ((A[0][0]*B[0][0]) % mod + (A[0][1]*B[1][0]) % mod) % mod
        y = ((A[0][0]*B[0][1]) % mod + (A[0][1]*B[1][1]) % mod) % mod
        w = ((A[1][0]*B[0][0]) % mod + (A[1][1]*B[1][0]) % mod) % mod
        z = ((A[1][0]*B[0][1]) % mod + (A[1][1]*B[1][1]) % mod) % mod

        A[0][0] = x
        A[0][1] = y
        A[1][0] = w
        A[1][1] = z

    A = [row.copy() for row in fibQMatrix]

    matrixPow(A, n-1)

    return A[0][0]


if __name__ == "__main__":
    T = int(stdin.readline())
    tests = []
    for _ in range(T):
        tests.append([int(x) for x in stdin.readline().split()])

    fibonacciSums(tests)
