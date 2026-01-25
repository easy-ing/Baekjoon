import sys
input = sys.stdin.readline

n = int(input())
members = []

for _ in range(n):
    age, name = input().split()
    members.append((int(age), name))

members.sort(key=lambda x: x[0])  # 나이만 기준으로 정렬 (stable)

print("\n".join(f"{age} {name}" for age, name in members))