test = input()
if test != test[::-1]:
    ans = test[::-1]+test
    print(ans)
else:
    print(test)
