def manachers_algorithm(s):
    if not s:
        return ""
    t = "^#" + "#".join(s) + "#$"
    c = 1
    d = 1
    p = [0] * len(t)
    for i in range(2, len(t)-1):
        mirror =  c-(i-c)
        p[i] = max(0, min(p[mirror], d-i))
        while t[i-1-p[i]] == t[i+p[i]+1]:
            p[i] += 1
            
        if i + p[i] > d:
            c = i
            d = i + p[i]
            
    (k, i) = max((p[i], i) for i in range(1, len(t)-1))
    start = (i-k)//2
    end = (i+k)//2
    return s[start:end]