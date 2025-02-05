times=int(input())
for i in range(times):
    a=input().split(" ")
    a=[int(x) for x in a]
    a.sort()
    print(f"{a[len(a)-1]} {a[len(a)-2]}")
    
