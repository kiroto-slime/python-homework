times = int(input())
for i in range(times):
    x = input()
    a=""
    b=""
    for e in x:
        if e == "4":
            a+="3"
            b+="1"
        else:
            a+=e
            b+="0"
    print(f"{int(a)} {int(b)}")
