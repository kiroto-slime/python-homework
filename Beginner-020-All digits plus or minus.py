j = int(input())
results = []
for i in range(j):
    nubmer = input()
    num = None
    plus = True
    for c in nubmer:
        if num == None:
            num = int(c)
        else:
            if plus:
                num = num + int(c)
            else:
                num = num - int(c)
            plus = not plus
    results.append(num)
for result in results:
    print(result)
#another
x = int(input())
for z in range(x):
    a = input()
    a1 = len(a)
    T = 1
    A = 0
    for i in range(1, a1):
        A = A + (int(a[i]) * T)
        T = T * -1
    A = A + int(a[0])
    print(A)
