from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])

    # 창고 주변을 빈 공간으로 한 겹 감싼다.
    board = [[''] * (m + 2) for _ in range(n + 2)]

    for i in range(n):
        for j in range(m):
            board[i + 1][j + 1] = storage[i][j]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for request in requests:
        target = request[0]

        # 크레인: 해당 종류의 컨테이너를 전부 제거
        if len(request) == 2:
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if board[i][j] == target:
                        board[i][j] = ''

        # 지게차: 외부와 연결된 target만 제거
        else:
            visited = [[False] * (m + 2) for _ in range(n + 2)]
            queue = deque([(0, 0)])
            visited[0][0] = True

            remove = []

            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if not (0 <= nx < n + 2 and 0 <= ny < m + 2):
                        continue

                    if visited[nx][ny]:
                        continue

                    # 빈 공간이면 외부에서 계속 이동할 수 있다.
                    if board[nx][ny] == '':
                        visited[nx][ny] = True
                        queue.append((nx, ny))

                    # 외부와 연결된 target 컨테이너 발견
                    elif board[nx][ny] == target:
                        visited[nx][ny] = True
                        remove.append((nx, ny))

            # BFS가 끝난 뒤 한꺼번에 제거
            for x, y in remove:
                board[x][y] = ''

    # 남아 있는 컨테이너 개수
    answer = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] != '':
                answer += 1

    return answer