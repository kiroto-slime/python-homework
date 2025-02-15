t= int(input())
all= []
for i in range(t):
    n= list(map(int, input().split()))
    all.append(n)
all.sort(key=lambda x:(-x[1], -x[2], x[0]))
for e in all:
    print(*e)#*[1, 90, 100] to 1 90 100
