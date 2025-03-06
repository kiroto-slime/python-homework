def getgrade(c):
    g=0
    if c in "0123456789":
        g=int(c)
    elif c=="X":
        g=10
    return g

spare="/"
strike="X"
normal="0123456789"

n=int(input())
for i in range(n):
    game=input().split()
    result,s,r=0,0,0
    l=len(game)
    while r<10:
        if game[s] in normal and game[s+1] in normal:
            result+=getgrade(game[s])+getgrade(game[s+1])
        elif game[s] in normal and game[s+1]==spare:
            result+=10+getgrade(game[s+2])
        elif game[s]==strike:
            if game[s+2]==spare:
                result+=10+10
            else:
                result+=10+getgrade(game[s+1])+getgrade(game[s+2])
            s-=1
        r+=1
        s+=2
    print(result)
