user1win=(["Y", "P"], ["O", "Y"], ["P", "O"])
times=int(input())
for i in range(times):
    x, y=input().split(",")
    if x==y:
        print("0")
    elif [x, y] in user1win:
        print("1")
    else:
        print("2")
