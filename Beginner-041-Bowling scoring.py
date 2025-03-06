def getgrade(c):
    g = 0
    if c in "0123456789":
        g = int(c)
    elif c == "X":
        g = 10
    return g

spare = "/"
strike = "X"
normal = "0123456789"
n = int(input())
for i in range(n):
    game = input().split()
    answer = 0
    s = 0
    r = 0
    l = len(game)
    while r < 10:
        if game[s] in normal and game[s+1] in normal:
            answer = answer + getgrade(game[s]) + getgrade(game[s+1])
        elif game[s] in normal and game[s+1] == spare:
            answer = answer + 10 + getgrade(game[s+2])
        elif game[s] == strike:
            if game[s+2] == spare:
                answer = answer + 10 + 10
            else:
                answer = answer + 10 + getgrade(game[s+1]) + getgrade(game[s+2])
            s = s-1
        r = r + 1
        s = s + 2
    print(answer)
