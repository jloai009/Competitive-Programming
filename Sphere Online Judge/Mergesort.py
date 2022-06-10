from sys import stdin
input = stdin.readline

def mergeSort(A):
    if len(A) < 2:
        return A
    
    mid = len(A) // 2 
    
    L = A[:mid]
    R = A[mid:]
    
    mergeSort(L)
    mergeSort(R)
    
    l = r = 0
    for i in range(len(A)):
        if r >= len(R) or l < len(L) and L[l] <= R[r]:
            A[i] = L[l]
            l  += 1
        else:
            A[i] = R[r]
            r += 1
    
    return A




A = list(map(int, input().split()))

mergeSort(A)

print(*A)