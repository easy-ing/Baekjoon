import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

subs = set()
for i in range(n):
    for j in range(i + 1, n + 1):
        subs.add(s[i:j])

print(len(subs))