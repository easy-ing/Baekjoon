from collections import deque

def solution(m, n, h, w, drops):
    INF = len(drops) + 1

    grid = [[INF] * n for _ in range(m)]

    for time, (r, c) in enumerate(drops, start=1):
        grid[r][c] = time

    row_min = []

    for r in range(m):
        dq = deque()
        temp = []

        for c in range(n):
            while dq and grid[r][dq[-1]] >= grid[r][c]:
                dq.pop()

            dq.append(c)

            if dq[0] <= c - w:
                dq.popleft()

            if c >= w - 1:
                temp.append(grid[r][dq[0]])

        row_min.append(temp)

    best_time = -1
    answer = [0, 0]

    for c in range(n - w + 1):
        dq = deque()

        for r in range(m):
            while dq and row_min[dq[-1]][c] >= row_min[r][c]:
                dq.pop()

            dq.append(r)

            if dq[0] <= r - h:
                dq.popleft()

            if r >= h - 1:
                top = r - h + 1
                current_time = row_min[dq[0]][c]

                if current_time > best_time:
                    best_time = current_time
                    answer = [top, c]

    return answer