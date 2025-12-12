def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def count_primes(start, end):
    """Count all prime numbers in the given range (inclusive)."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == "__main__":
    start = 1
    end = 100

    prime_numbers = count_primes(start, end)

    print(f"Prime numbers from {start} to {end}:")
    print(prime_numbers)
    print(f"\nTotal count: {len(prime_numbers)} prime numbers")
