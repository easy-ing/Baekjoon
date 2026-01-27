import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cnt = Counter(cards)

m = int(input())
queries = list(map(int, input().split()))

print(" ".join(str(cnt[q]) for q in queries))