n=int(input())
ppos=[1,2,4,8,16]
for i in range(n):
    s=input().strip()
    x=int(s,16)
    b=bin(x)[2:].zfill(16)
    arr=[0]*22
    idx=0
    for e in range(1,22):
        if e not in ppos:
            arr[e]=int(b[idx])
            idx+=1
    for p in ppos:
        sm=0
        for e in range(1,22):
            if e&p:
                sm^=arr[e]
        arr[p]=sm
    print(''.join(str(arr[p]) for p in ppos))
