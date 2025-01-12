x = int(input())
unhappy_cycle = [4, 16, 37, 58, 89, 145, 42, 20]

for i in range(x):
    y = int(input())
    seen = []

    while True:
        if y == 1:
            print("T")
            break
        if y in unhappy_cycle:
            print("F")
            break
        if y in seen:
            print("F")
            break
        seen.append(y)
        y = sum(int(e) ** 2 for e in str(y))
