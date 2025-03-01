time=int(input())
f=[1]
ftotal=[0]
inputs=[]
for i in range(time):
    inp=int(input())
    if inp<25:
      inputs.append(inp)
    else :
      inputs.append(25)
max = max(inputs)
for i in range(1,max+1):
    f.append(f[-1]*i)
    ftotal.append(ftotal[-1]+f[-1])
for i in inputs:
    print(str(ftotal[i]).zfill(6)[-6:])
