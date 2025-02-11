times=int(input())
for i in range(times):
    a,b,c=input().split()
    a,b=int(a),int(b)
    n=0
    for num in range(a, b + 1):
        if c in str(num):
            n += 1
    print(n)
