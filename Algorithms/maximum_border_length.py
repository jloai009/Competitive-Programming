def maximum_border_length(w):
    n = len(w)
    f = [0] * n                 # init f[0] = 0
    k=0                         # current longest border length
    for i in range(1, n):       # compute f[i]
        while w[k] != w[i] and k > 0:
            k = f[k - 1]        # mismatch: try the next border
        if w[k] == w[i]:        # last characters match
            k += 1              # we can increment the border length
        f[i] = k                # we found the maximal border of w[:i + 1]
    return f
