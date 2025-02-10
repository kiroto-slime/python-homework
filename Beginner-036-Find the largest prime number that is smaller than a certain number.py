def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
times=int(input())
for i in range(times):
    x=int(input())
    if x==2:
        print(2)
        continue
    for e in range(2,x):
        if prime(e):
            max_x=e
    print(max_x)
