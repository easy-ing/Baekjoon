import sys

input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

points.sort()  # (x, y) 튜플이라 x -> y 순으로 자동 정렬됨

out = []
for x, y in points:
    out.append(f"{x} {y}")
print("\n".join(out))