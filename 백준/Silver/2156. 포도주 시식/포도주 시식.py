import sys
input = sys.stdin.readline

n = int(input())
wine = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n + 1)

if n >= 1:
    dp[1] = wine[1]
if n >= 2:
    dp[2] = wine[1] + wine[2]

for i in range(3, n + 1):
    dp[i] = max(
        dp[i - 1],                          # 현재 잔 안 마심
        dp[i - 2] + wine[i],               # 현재 잔만 마심
        dp[i - 3] + wine[i - 1] + wine[i]  # 이전 잔 + 현재 잔 마심
    )

print(dp[n])