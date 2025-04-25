import sys
def Goldbach(n, prime_set):
    count= 0
    for p in prime_set:
        if p > n//2:
            break
        if (n-p) in prime_set:
            count+= 1
    return count

def sieve(limit):
    is_prime= [False, False]+[True]*(limit-1)
    for i in range(2, int(limit**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i):
                is_prime[j]= False # marking multiples of i as non-prime
    return {i for i, val in enumerate(is_prime) if val} # enumerate returns (index, value) pairs

prime_set= sieve(32768) # Pre_computer primes up to 32768
for line in sys.stdin:
    n= int(line.strip())
    if n== 0:
        break
    print(Goldbach(n, prime_set))
