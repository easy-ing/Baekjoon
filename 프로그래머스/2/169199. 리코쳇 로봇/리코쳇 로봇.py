from collections import deque


def solution(board):
    n = len(board)
    m = len(board[0])

    # 시작 위치와 목표 위치 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)

    # BFS
    queue = deque()
    queue.append((start[0], start[1], 0))

    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True

    directions = [
        (-1, 0),  # 상
        (1, 0),   # 하
        (0, -1),  # 좌
        (0, 1)    # 우
    ]

    while queue:
        x, y, count = queue.popleft()

        # 목표 도착
        if (x, y) == goal:
            return count

        for dx, dy in directions:
            nx, ny = x, y

            # 장애물이나 가장자리를 만날 때까지 이동
            while True:
                next_x = nx + dx
                next_y = ny + dy

                # 게임판 밖이거나 장애물이면 현재 위치에서 정지
                if (
                    next_x < 0 or next_x >= n or
                    next_y < 0 or next_y >= m or
                    board[next_x][next_y] == 'D'
                ):
                    break

                nx, ny = next_x, next_y

            # 이동할 수 없거나 이미 방문한 위치라면 생략
            if (nx, ny) == (x, y):
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))

    return -1