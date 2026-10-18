def solution(n):
    MOD = 1_000_000_007

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if i >= 2:
            dp[i] += dp[i - 2] * 3
        if i >= 4:
            for j in range(4, i + 1, 2):
                dp[i] += dp[i - j] * 2
        dp[i] %= MOD

    return dp[n]