a= int(input())
for i in range(1, a+1):
    print("  "*(a-i), end= "")
    for e in range(1, i+1):
        print(e, end= " ")
    for g in range(i-1, 0, -1):
        print(g, end= " ")
    print()
