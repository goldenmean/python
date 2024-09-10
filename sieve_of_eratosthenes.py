''' Implement Sieve of Eratosthenes alghorithm to find all prime numbers up to n
'''
'''
def sieve_of_eratosthenes(N):
    # Initialize a list to keep track of prime numbers
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Start with the first prime number, which is 2
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i as non-prime
            for j in range(i * i, N, i):
                is_prime[j] = False

    # Collect all prime numbers
    primes = [i for i in range(N) if is_prime[i]]
    return primes

# Example usage:
N = 50
primes = sieve_of_eratosthenes(N)
print(f"Prime numbers less than {N}: {primes}")

'''


def dynamic_prime_generator():
    D = {}  # Dictionary to hold multiples of primes
    q = 2   # Starting integer to check for primality

    while True:
        if q not in D:
            # q is a new prime number
            yield q
            # Mark the first multiple of q that is not already marked
            D[q * q] = [q]
        else:
            # q is not a prime, it is a multiple of some prime numbers
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            # Remove q from the dictionary
            del D[q]
        q += 1

# Example usage:
gen = dynamic_prime_generator()
for _ in range(10):
    print(next(gen))