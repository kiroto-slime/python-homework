times= int(input())
for i in range(times):
    a= input().split(" ")
    b= input().split(" ")
    seen= set()
    for i in a[1:]:
       for e in b[1:]:
           if i==e:
               seen.add(i)
    print(len(seen))   
#another
times= int(input())
for i in range(times):
    a= input().split(" ")
    b= input().split(" ")
    y=0
    for i in a[1:]:
       if i in b[1:]:
           y+=1
    print(y) 
