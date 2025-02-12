times=int(input())
for i in range(times):
    a,b=input().split(", ")
    A=0
    B=0
    for i in range(len(a)):
        if a[i] == b[i]:
            A+=1
    used= set()
    for i, digit in enumerate(a):
        if digit in b and a[i] != b[i]:
            for e in range(len(b)):
                if b[e] == digit and e not in used and a[e] != b[e]:
                    B += 1
                    used.add(e)
                    break
    print(f"{A}A{B}B")
#another
times=int(input())
for i in range(times):
    a,b=input().split(", ")
    A=0
    B=0
    for e in range(len(b)):
        if a[e]==b[e]:
            A+=1
        elif a[e] in b:
            B+=1
    print(f"{A}A{B}B")
