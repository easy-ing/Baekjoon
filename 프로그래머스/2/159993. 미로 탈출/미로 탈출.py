from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    # 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # S, L, E 위치 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)

    def bfs(start, target):
        queue = deque([(start[0], start[1], 0)])
        visited = [[False] * m for _ in range(n)]
        visited[start[0]][start[1]] = True

        while queue:
            x, y, distance = queue.popleft()

            # 목적지에 도착
            if (x, y) == target:
                return distance

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                # 미로 범위 안이고, 벽이 아니며, 방문하지 않은 경우
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != 'X' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, distance + 1))

        # 목적지에 도달할 수 없음
        return -1

    # 1. 시작점 → 레버
    to_lever = bfs(start, lever)

    if to_lever == -1:
        return -1

    # 2. 레버 → 출구
    to_exit = bfs(lever, exit)

    if to_exit == -1:
        return -1

    return to_lever + to_exit