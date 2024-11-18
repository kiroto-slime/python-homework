a, b, c = input().split(" ")
A = float(a)
B = float(b)
C = float(c)
ai = B*B-4*A*C
if ai > 0:
    a1 = (-B+ai**0.5)/(2*A)
    a3 = (-B-ai**0.5)/(2*A)
    if a1 > a3:
        ans=(f"{a3} {a1}")
    else:
        ans=(f"{a1} {a3}")
    print(ans)
elif ai < 0:
    print("NoSolution")
else:
    a2 = (-B)/2*A
    print(f"DR={a2}")
