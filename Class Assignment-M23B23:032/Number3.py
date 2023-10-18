import math

def get_prime_factors(n):
    factors = {}
    # Divide n by 2 until it's odd
    while n % 2 == 0:
        if 2 in factors:
            factors[2] += 1
        else:
            factors[2] = 1
        n = n // 2
    # Now n is odd
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n = n // i
    if n > 1:
        factors[n] = 1
    return factors

def find_smallest_multiple_factors(n):
    lcm = 1
    factors = {}
    
    for i in range(2, n + 1):
        prime_factors = get_prime_factors(i)
        for factor, count in prime_factors.items():
            if factor in factors:
                factors[factor] = max(factors[factor], count)
            else:
                factors[factor] = count

    for factor, count in factors.items():
        lcm *= factor ** count

    return lcm, list(factors.keys())

n = 13
smallest_multiple, factors = find_smallest_multiple_factors(n)

print(f"The smallest multiple of the first {n} numbers is: {smallest_multiple}")
print(f"The prime factors of the first {n} numbers are: {factors}")
