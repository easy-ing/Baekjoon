n = int(input())
MOD = 1_000_000_000

dp = [[0] * 10 for _ in range(n + 1)]

# 길이 1 초기값
for i in range(1, 10):
    dp[1][i] = 1

# 길이 2부터 n까지 채우기
for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][8]

    for j in range(1, 9):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD

# 마지막 자리 0~9 합치기
print(sum(dp[n]) % MOD)