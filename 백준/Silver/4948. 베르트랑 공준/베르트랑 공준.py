import sys

def sieve(limit: int):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    r = int(limit ** 0.5)
    for i in range(2, r + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime

data = sys.stdin.read().strip().split()
nums = list(map(int, data))

max_n = 0
for x in nums:
    if x == 0:
        break
    if x > max_n:
        max_n = x

limit = 2 * max_n
is_prime = sieve(limit)

# prefix sum
prefix = [0] * (limit + 1)
cnt = 0
for i in range(1, limit + 1):
    if is_prime[i]:
        cnt += 1
    prefix[i] = cnt

out = []
for n in nums:
    if n == 0:
        break
    out.append(str(prefix[2 * n] - prefix[n]))

print("\n".join(out))