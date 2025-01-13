times= int(input())
for i in range(times):
    cycle= [0,1,2,0]
    a= input().split(",")
    for e in range(len(a)):
        if a[e]=="Y":
            a[e]=1
        elif a[e]=="O":
            a[e]=0
        elif a[e]=="P":
            a[e]=2
    if a[0]==a[1]:
        print("0")
        continue
    for h in range(0,3):
        if cycle[h]==a[0]:
            if a[1]== cycle[h+1]:
                print("1")
            else:
                print("2")
