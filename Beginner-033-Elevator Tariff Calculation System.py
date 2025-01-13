times= int(input())
for i in range(times):
    up=0
    down=0
    C_CPP_= input()
    z= input().split(",")
    for e in range(len(z)-1):
        first= int(z[e])
        next= int(z[e+1])
        if first>next:
            down+= first-next
        elif first<next:
            up+= next-first
    print((up*20)+(down*10))
