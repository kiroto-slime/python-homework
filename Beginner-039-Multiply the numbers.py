times=int(input())
for i in range(times):
    x=int(input())
    g=[]
    for e in range(9,1,-1):
        while x%e==0:
            g.append(e)
            x//=e
    g.sort()
    if len(g)==0 or x!=1:
        print(-1,end="")
    else:
        for j in g:
            print(j,end="")
    print()
