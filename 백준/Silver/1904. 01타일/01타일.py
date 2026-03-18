import sys

n = int(sys.stdin.readline())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    a, b = 1, 2  # dp[1], dp[2]

    for _ in range(3, n + 1):
        a, b = b, (a + b) % 15746

    print(b)