a= int(input())
for i in range(1, a+1):
    for e in range(1, i+1):
        print(e, end= " ")
    print()
print()
for i in range(a, 0,-1):
    for e in range(1, i+1):
        print(e, end= " ")
    print()
print()
for i in range(a, 0,-1):
    for e in range(a, a-i, -1):
        print(e, end= " ")
    print()
print()
for i in range(1, a+1):
    print("  "*(a-i), end= "")
    for e in range(1, i+1):
        print(e, end= " ")
    print()
