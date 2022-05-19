# Kattis - Casting Spells
# https://open.kattis.com/problems/castingspells

s = input()

t = "$#" + "#".join(s) +"#^"
p = [0]*len(t)
c = d = 1
for i in range(2, len(p)-1):
    mirror = c-(i-c)
    p[i] = max(0, min(p[mirror], d-i))
    while t[i+p[i]+1] == t[i-p[i]-1]:
        p[i] += 1
    if i + p[i] > d:
        c = i
        d = i + p[i]

ans = 0

for i in range(1, len(p)-1):
    if p[i] % 2 == 0 and p[i] > ans:
        good_rad = (p[i]//4)*2
        offset = ans//2 + 2
        while offset <= good_rad:
            if p[i+offset] >= offset:
                ans = max(ans, offset*2)
            offset += 2

print(ans)