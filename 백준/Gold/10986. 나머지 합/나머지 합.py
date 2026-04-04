import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

count = [0] * M
prefix = 0

# 누적합의 나머지가 0인 경우를 위해 미리 1개 넣어둠
count[0] = 1

for num in arr:
    prefix = (prefix + num) % M
    count[prefix] += 1

answer = 0
for c in count:
    answer += c * (c - 1) // 2

print(answer)