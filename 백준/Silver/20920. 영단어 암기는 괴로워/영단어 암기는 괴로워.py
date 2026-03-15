import sys

input = sys.stdin.readline

N, M = map(int, input().split())

word_count = {}

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        word_count[word] = word_count.get(word, 0) + 1

result = sorted(word_count.keys(), key=lambda x: (-word_count[x], -len(x), x))

print("\n".join(result))