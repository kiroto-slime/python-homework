#狗換算成人的年紀
z = int(input())
ans = "Wrong"
if z > 2:
    ans = (z-2) * 4 + 21
elif 0 < z <= 2:
    ans = z * 10.5
print(ans)
