times= int(input())
for i in range(times):
    n= input()
    while True:
        if n!=n[::-1]:
            a=int(n)
            b=int(n[::-1])
            n=str(a+b)
        else:
            print(n)
            break
