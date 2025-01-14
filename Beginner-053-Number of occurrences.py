z= int(input())
for i in range(z):
    wow= [0,0,0,0,0,0,0,0,0,0]
    x= int(input())
    for e in range(1,x+1):
        num=e
        while num:
            wow[num%10]+=1
            num//=10
    for h in wow:
        print(h,end=" ")
    print()
