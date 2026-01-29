import sys

input = sys.stdin.readline

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False

    # n - 1 = d * 2^s (d odd)
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    def check(a: int) -> bool:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False

    # Deterministic for n < 4,759,123,141
    for a in (2, 7, 61):
        if a % n == 0:
            return True
        if not check(a):
            return False
    return True

def next_prime_ge(n: int) -> int:
    if n <= 2:
        return 2
    if n % 2 == 0:
        n += 1
    while not is_prime(n):
        n += 2
    return n

t = int(input().strip())
out = []
for _ in range(t):
    n = int(input().strip())
    out.append(str(next_prime_ge(n)))

print("\n".join(out))