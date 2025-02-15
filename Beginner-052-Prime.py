import math
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):#sqrt(n)是n的平方根
        if n % i == 0:
            return False
    return True
while True:
    n = int(input())
    if n == 0:
        break  
    count = 0
    for p1 in range(2, n // 2 + 1):
        p2 = n - p1 
        if prime(p1) and prime(p2):
            count += 1
    print(count)
