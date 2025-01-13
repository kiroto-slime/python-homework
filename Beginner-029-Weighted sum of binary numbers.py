try:
    while True:
        a= input()
        if a== "EOF" or a== "":
            break
        a= a.split(" ")
        w= int(a[0])
        h= int(a[1])
        print((w*4)+(h*6))
except EOFError:
    pass
