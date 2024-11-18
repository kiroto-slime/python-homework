year = int(input())
ans = "a normal year"
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    ans = "a leap year"
print(ans)
