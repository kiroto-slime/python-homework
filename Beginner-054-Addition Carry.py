a,b="1","1"
while True: 
    carry=0
    a,b=input().split(" ")
    if a=="0" and b=="0":
        break
    a="".join(reversed(a))
    b="".join(reversed(b))
    max_len=max(len(a),len(b))
    for i in range(max_len):
        if int(a[i])+int(b[i])>=10:
           carry+=1 
    if carry==1:
        print(f"{carry} carry operation.")
    elif carry>1:
        print(f"{carry} carry operations.")
    else:
        print("No carry operation.")
