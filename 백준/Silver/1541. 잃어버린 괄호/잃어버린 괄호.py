import sys

expression = sys.stdin.readline().strip()

parts = expression.split('-')

answer = sum(map(int, parts[0].split('+')))

for part in parts[1:]:
    answer -= sum(map(int, part.split('+')))

print(answer)