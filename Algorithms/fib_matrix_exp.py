def fib(n):
    if n <= 1:
        return n

    fibQMatrix = [[1, 1], [1, 0]]

    def matrixPow(A, n):
        if n <= 1:
            return A
        matrixPow(A, n//2)
        mult(A, A)
        
        if n%2 != 0:
            mult(A, fibQMatrix)

    def mult(A, B):
        x = A[0][0]*B[0][0] + A[0][1]*B[1][0]
        y = A[0][0]*B[0][1] + A[0][1]*B[1][1]
        w = A[1][0]*B[0][0] + A[1][1]*B[1][0]
        z = A[1][0]*B[0][1] + A[1][1]*B[1][1]

        A[0][0] = x
        A[0][1] = y
        A[1][0] = w
        A[1][1] = z

    A = [row.copy() for row in fibQMatrix]

    matrixPow(A, n-1)

    return A[0][0]
