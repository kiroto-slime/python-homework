times=int(input())
for i in range(times):
    a,b,c=map(int,input().split())
    print(a**b%c)
