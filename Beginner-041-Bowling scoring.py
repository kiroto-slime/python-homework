t=int(input())
for _ in range(t):
    rolls=input().split()
    a=[]
    for r in rolls:
        if r=="X" and len(a)<=18:
            a.extend([" ","X"])
        else:
            a.append(r)
    s=0
    for i in range(0,18,2):
        c=0
        f=[a[i],a[i+1]] if a[i]!=" " else [" ",a[i+1]]
        n=[]
        m=[]
        if "X" in f or "/" in f:
            if a[i+1]=="X":
                n=[a[i+2],a[i+3]]
                if a[i+3]=="X":
                    m=[a[i+4],a[i+5]]
            elif a[i+1]=="/":
                n=[a[i+2],a[i+3]]
            else:
                n=[a[i+1],a[i+2]]
        if "X" in f:
            c=10
            if "X" in n:
                c+=10
                if m and "X" in m:
                    c+=10
                elif m:
                    c+=int(m[0])
            elif "/" in n:
                c+=10
            else:
                c+=int(n[0])+int(n[1])
        elif "/" in f:
            c=10
            if "X" in n:
                c+=10
            else:
                c+=int(n[0])
        else:
            c+=int(f[0])+int(f[1])
        s+=c
    if len(a)<21:
        a.append(" ")
    c=0
    if "X" in a[-3]:
        c=10
        if "X" in a[-2]:
            c+=10
            c+=10 if "X" in a[-1] else int(a[-1])
        elif "/" in a[-2:]:
            c+=10
        else:
            c+=int(a[-2])+int(a[-1])
    elif "/" in a[-3:]:
        c=10
        c+=10 if "X" in a[-1] else int(a[-1])
    else:
        c+=int(a[-3])+int(a[-2])
    print(s+c)


#another
import sys;t=int(sys.stdin.readline())
for _ in range(t):
 a=[];r=sys.stdin.readline().split();[a.extend([" ","X"])if x=="X"and len(a)<=18 else a.append(x)for x in r];s=0
 for i in range(0,18,2):
  f=a[i:i+2];c=0;n=m=[]
  if"X"in f or"/"in f:
   if a[i+1]=="X":n=a[i+2:i+4]
   elif a[i+1]=="/":n=a[i+2:i+4]
   else:n=a[i+1:i+3]
   if a[i+1]=="X"and a[i+3]=="X":m=a[i+4:i+6]
  if"X"in f:
   c=10
   if"X"in n:
    c+=10
    if m and"X"in m:c+=10
    elif m:c+=int(m[0])
   elif"/"in n:c+=10
   else:c+=int(n[0])+int(n[1])
  elif"/"in f:c=10;c+=10 if"X"in n else int(n[0])
  else:c+=int(f[0])+int(f[1])
  s+=c
 if len(a)<21:a.append(" ");c=0
 if"X"in a[-3]:
  c=10
  if"X"in a[-2]:c+=10;c+=10 if"X"in a[-1]else int(a[-1])
  elif"/"in a[-2:]:c+=10
  else:c+=int(a[-2])+int(a[-1])
 elif"/"in a[-3:]:c=10;c+=10 if"X"in a[-1]else int(a[-1])
 else:c+=int(a[-3])+int(a[-2])
 print(s+c)
    else:
        c+=int(a[-3])+int(a[-2])
    print(s+c)
