def hamming_code(s):
    x= int(s,16)
    arr= [0]*21
    for i in range(16):
        arr[i + i//4 + 1]= (x>>i)&1
    for i in range(4, -1, -1):
        parity= sum(arr[j] for j in range(1, 21) if j & (1<<i))%2
        arr[1<<i]= parity
    return ''.join(str(arr[1<<i]) for i in range(5))
n= int(input())
for e in range(n):
    s= input().strip()
    print(hamming_code(s))
