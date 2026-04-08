import sys

input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))

times.sort()

prefix = 0
answer = 0

for t in times:
    prefix += t
    answer += prefix

print(answer)