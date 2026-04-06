import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [input().strip() for _ in range(N)]

width = M - K + 1
window_sum = [0] * width
rows_queue = deque()

answer = K * K

for i in range(N):
    row = board[i]

    # 현재 행에서 각 칸이 "W 시작 체스판" 기준 mismatch인지 계산
    mismatch = [0] * M
    for j in range(M):
        expected = 'W' if (i + j) % 2 == 0 else 'B'
        if row[j] != expected:
            mismatch[j] = 1

    # 현재 행에서 가로 길이 K 구간들의 mismatch 개수
    row_windows = [0] * width
    current = sum(mismatch[:K])
    row_windows[0] = current

    for j in range(1, width):
        current += mismatch[j + K - 1] - mismatch[j - 1]
        row_windows[j] = current

    # 세로 슬라이딩 누적
    rows_queue.append(row_windows)
    for j in range(width):
        window_sum[j] += row_windows[j]

    if len(rows_queue) > K:
        old = rows_queue.popleft()
        for j in range(width):
            window_sum[j] -= old[j]

    # K행이 쌓였으면 정답 후보 계산
    if len(rows_queue) == K:
        for j in range(width):
            wrong_w = window_sum[j]
            wrong_b = K * K - wrong_w
            repaint = wrong_w if wrong_w < wrong_b else wrong_b
            if repaint < answer:
                answer = repaint

print(answer)