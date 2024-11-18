l = int(input())
for h in range(l):
    n = int(input())
    j = 2
    pi = 3
    plus = True
    for i in range(n - 1):
        k = (4 / (j * (j + 1) * (j + 2)))
        if plus:
            pi += k
        else:
            pi -= k
        j += 2
        plus = not plus
    print(pi)
