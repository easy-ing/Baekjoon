import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0] * (K + 1)

for _ in range(N):
    W, V = map(int, input().split())
    
    for weight in range(K, W - 1, -1):
        dp[weight] = max(dp[weight], dp[weight - W] + V)

print(dp[K])