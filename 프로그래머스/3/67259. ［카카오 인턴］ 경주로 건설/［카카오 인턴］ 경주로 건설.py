import heapq

def solution(board):
    n = len(board)

    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    INF = float('inf')

    # dist[x][y][d] : (x, y)에 d 방향으로 도착하는 최소 비용
    dist = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    pq = []

    # 시작점에서 첫 이동
    for d in range(4):
        nx = dx[d]
        ny = dy[d]

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            dist[nx][ny][d] = 100
            heapq.heappush(pq, (100, nx, ny, d))

    while pq:
        cost, x, y, direction = heapq.heappop(pq)

        # 이미 더 저렴한 경로가 존재하면 생략
        if cost > dist[x][y][direction]:
            continue

        # 네 방향으로 이동
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 범위 및 벽 확인
            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if board[nx][ny] == 1:
                continue

            # 직진이면 100원, 방향 전환이면 600원
            new_cost = cost + 100

            if direction != d:
                new_cost += 500

            # 최소 비용 갱신
            if new_cost < dist[nx][ny][d]:
                dist[nx][ny][d] = new_cost
                heapq.heappush(pq, (new_cost, nx, ny, d))

    # 도착점에 도달하는 네 방향 중 최솟값
    return min(dist[n-1][n-1])