import sys
import math

input = sys.stdin.readline

N = int(input().strip())
pos = [int(input().strip()) for _ in range(N)]

# 인접 간격들의 gcd 구하기
g = pos[1] - pos[0]
for i in range(2, N):
    g = math.gcd(g, pos[i] - pos[i-1])

# 필요한 추가 나무 수 계산
ans = 0
for i in range(1, N):
    ans += (pos[i] - pos[i-1]) // g - 1

print(ans)