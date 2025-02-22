b={
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17,
    'I': 34, 'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23,
    'Q': 24, 'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30,
    'Y': 31, 'Z': 33
}
def findb(num1):
    valid_h=[]
    for h in sorted(b.keys()):
        if is_valid_id(h, num1):
            valid_h.append(h)
    return "".join(valid_h)
def is_valid_id(h, num1):
    num2=b[h]
    n1, n2=divmod(num2, 10)
    numbers=[n1, n2]+[int(d) for d in num1]
    weights=[1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    total=sum(x*w for x, w in zip(numbers, weights))
    return total%10==0
n = int(input())
for i in range(n):
    digits = input()
    print(findb(digits))
