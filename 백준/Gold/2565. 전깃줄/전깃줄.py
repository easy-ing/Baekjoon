import sys

input = sys.stdin.readline

n = int(input())
wires = []

for _ in range(n):
    a, b = map(int, input().split())
    wires.append((a, b))

# A 전봇대 기준 정렬
wires.sort()

# B 값만 추출
b_list = [b for a, b in wires]

# LIS 구하기 (O(N^2))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if b_list[j] < b_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

lis_length = max(dp)

# 최소로 제거해야 하는 전깃줄 수
print(n - lis_length)