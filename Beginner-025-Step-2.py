times = int(input())
inputs = [int(input()) for _ in range(times)]
max_input = max(inputs)
last_not0 = [1] * (max_input + 1)

for i in range(2, max_input + 1):
    last_not0[i] = last_not0[i - 1] * i
    while last_not0[i] % 10 == 0:
        last_not0[i] //= 10

    last_not0[i] %= 100000

for i in inputs:
    print(last_not0[i] % 10)
