x= int(input())
for z in range(x):
    a= input()
    T= 1
    A= 0
    for i in range(1, len(a)):
        A+= (int(a[i])*T)
        T*= -1
    A+=int(a[0])
    print(A)
