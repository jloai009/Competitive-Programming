for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    
    # Codeforces 1676H2 Maximum Crossings
    # https://codeforces.com/contest/1676/problem/H2

    def mergeSort(arr):
        global ans
        if len(arr) < 2:
            return arr
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        pL = pR = 0
        for i in range(len(arr)):
            if pR == len(R) or pL<len(L) and L[pL]<R[pR]:
                arr[i] = L[pL]
                ans += pR
                pL += 1
            else:
                arr[i] = R[pR]
                pR += 1
        return arr

    mergeSort(a)

    print(ans)