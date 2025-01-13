times = int(input())
for i in range(times):
    num = input()
    sum = 0
    for e in range(0, len(num)):
        NumberOfCard = 16-e
        if NumberOfCard % 2:
            number = int(num[e])*1
        else:
            number = int(num[e])*2
        if number >= 10:
            sum += (number-9)
        else:
            sum += number
    if sum % 10 == 0:
        print("T")
    else:
        print("F")
