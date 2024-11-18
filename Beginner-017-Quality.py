b= int(input())#(1≤n≤10)
for e in range(b):
    x= int(input())#2≤x≤65535
    if x>1:
        for i in range(2, int(x/2)+1):
            if x% i == 0:
                print("N")
                break
        else:
            print("Y")
