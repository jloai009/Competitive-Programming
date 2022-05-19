def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    merge_sort(L)
    merge_sort(R)
    l = r = 0
    for i in range(len(arr)):
        if r == len(R) or l < len(L) and L[l] <= R[r]:
            arr[i] = L[l]
            l += 1
        else:
            arr[i] = R[r]
            r += 1
    return arr
