times= int(input())
for i in range(times):
    n= input()

    while True:
        if n!=n[::-1]:
            a=int(n)
            b=int(n[::-1])
            n=a+b
            n=str(n)
        else:
            print(n)
            break
