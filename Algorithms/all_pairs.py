def all_pairs(L):
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            
            yield (L[i], L[j])
