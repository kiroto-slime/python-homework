num= int(input())
for i in range(num):
    test = input()
    test= test.replace(" ", "")
    if test != test[::-1]:
        ans = test[::-1]+test
        print("N")
    else:
        print("Y")
