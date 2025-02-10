times=int(input())
for i in range(times):
    x=input()
    s=0
    combo=0
    for e in x:
        if e=="O":
            combo+=1
            s+=combo
        elif e=="X":
            combo=0
    print(s)   
