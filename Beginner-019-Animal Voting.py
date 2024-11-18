tigers = 0
lions = 0

for i in range(9):
    j = input()
    if j == "Tiger":
        tigers += 1
    elif j == "Lion":
        lions += 1
if (tigers > lions):
    print("Tiger")
else:
    print("Lion")
