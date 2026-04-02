import sys

input = sys.stdin.readline

N, K = map(int, input().split())
temps = list(map(int, input().split()))

# 처음 K일의 합
current_sum = sum(temps[:K])
max_sum = current_sum

# 슬라이딩 윈도우
for i in range(K, N):
    current_sum += temps[i] - temps[i - K]
    max_sum = max(max_sum, current_sum)

print(max_sum)