import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

S = input().strip()

positions = [[] for _ in range(26)]

for i, ch in enumerate(S):
    positions[ord(ch) - ord('a')].append(i)

q = int(input())
answers = []

for _ in range(q):
    alpha, l, r = input().split()
    l = int(l)
    r = int(r)

    arr = positions[ord(alpha) - ord('a')]
    count = bisect_right(arr, r) - bisect_left(arr, l)
    answers.append(str(count))

print('\n'.join(answers))