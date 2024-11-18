num= int(input())
for i in range(num):
    x, y= input().split()
    for e in x:
        ascii= ( ord(e) - ord('A') + int(y) ) % 26 + ord('A')
        print(chr(ascii), end="")
    print()
