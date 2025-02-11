times = int(input())
t = {}
for i in range(times):
    data = input().split()
    c = data[0]
    if c in t:
        t[c] += 1
    else:
        t[c] = 1
for e in sorted(t):
    print(e, t[e])
