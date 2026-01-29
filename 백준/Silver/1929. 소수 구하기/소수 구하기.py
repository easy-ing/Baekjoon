import sys

input = sys.stdin.readline

M, N = map(int, input().split())

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체
limit = int(N ** 0.5)
for i in range(2, limit + 1):
    if is_prime[i]:
        step_start = i * i
        for j in range(step_start, N + 1, i):
            is_prime[j] = False

# 출력 (빠르게 모아서 출력)
out = []
for x in range(M, N + 1):
    if is_prime[x]:
        out.append(str(x))

print("\n".join(out))