import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 1-based index 사용
prefix = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        prefix[i][j] = (
            prefix[i - 1][j]
            + prefix[i][j - 1]
            - prefix[i - 1][j - 1]
            + row[j - 1]
        )

answers = []

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = (
        prefix[x2][y2]
        - prefix[x1 - 1][y2]
        - prefix[x2][y1 - 1]
        + prefix[x1 - 1][y1 - 1]
    )
    answers.append(str(result))

print('\n'.join(answers))