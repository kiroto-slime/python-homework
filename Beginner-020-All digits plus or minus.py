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
