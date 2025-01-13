times= int(input())
for i in range(times):
    a= input()
    b= input()
    seen= set()
    for i in a:
       for e in b:
           if i==e:
               seen.add(i)
    seen= sorted(seen)
    if not seen:
        print("N")
        continue
    for g in seen:
        print(g,end="")
    print()   
