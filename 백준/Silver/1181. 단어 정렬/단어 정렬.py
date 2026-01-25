import sys
input = sys.stdin.readline

n = int(input())
words = {input().strip() for _ in range(n)}  # 중복 제거

words = sorted(words, key=lambda w: (len(w), w))  # (길이, 사전순)

print("\n".join(words))