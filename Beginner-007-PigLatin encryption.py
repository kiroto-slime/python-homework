y=input()
if y [0] in ["a", "e", "i", "o", "u"] :
    ans = (f"{y}way")
    print(ans)
else :
    a = y[0]
    y = y[1:]
    print(f"{y}{a}ay")
