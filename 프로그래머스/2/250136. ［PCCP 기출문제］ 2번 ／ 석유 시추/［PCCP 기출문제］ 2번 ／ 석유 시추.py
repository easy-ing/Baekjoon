from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])

    # 각 열에서 얻을 수 있는 석유량
    oil = [0] * m

    # 상, 하, 좌, 우
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 모든 석유 덩어리를 한 번씩만 탐색
    for r in range(n):
        for c in range(m):

            if land[r][c] == 0:
                continue

            # 하나의 석유 덩어리 탐색
            queue = deque([(r, c)])
            land[r][c] = 0

            size = 0
            columns = set()

            while queue:
                x, y = queue.popleft()

                size += 1
                columns.add(y)

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < n and 0 <= ny < m:
                        if land[nx][ny] == 1:
                            land[nx][ny] = 0
                            queue.append((nx, ny))

            # 이 덩어리가 걸쳐 있는 모든 열에 크기를 더함
            for col in columns:
                oil[col] += size

    return max(oil)