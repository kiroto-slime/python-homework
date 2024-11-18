num= int(input())
for i in range(num):
    num1= input()
    num2= input()
    result=0
    for abc in range(0,len(num1)):
        if num1[abc] != num2[abc]:
            result+=1
    print(result)
