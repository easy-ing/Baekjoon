import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input().strip())
cards = list(map(int, input().split()))
cards.sort()

M = int(input().strip())
queries = list(map(int, input().split()))

ans = []
for x in queries:
    idx = bisect_left(cards, x)
    if idx < N and cards[idx] == x:
        ans.append("1")
    else:
        ans.append("0")

print(" ".join(ans))