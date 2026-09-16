from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]
    answer = []

    # 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(n):
        for c in range(m):

            # 바다이거나 이미 방문한 칸이면 넘어감
            if maps[r][c] == 'X' or visited[r][c]:
                continue

            # 새로운 섬 발견
            queue = deque([(r, c)])
            visited[r][c] = True

            food = 0

            while queue:
                cr, cc = queue.popleft()

                # 현재 칸의 식량 더하기
                food += int(maps[cr][cc])

                # 상, 하, 좌, 우 탐색
                for dr, dc in directions:
                    nr = cr + dr
                    nc = cc + dc

                    # 지도 범위를 벗어나면 무시
                    if nr < 0 or nr >= n or nc < 0 or nc >= m:
                        continue

                    # 바다거나 이미 방문했으면 무시
                    if maps[nr][nc] == 'X' or visited[nr][nc]:
                        continue

                    visited[nr][nc] = True
                    queue.append((nr, nc))

            # 하나의 섬 탐색 완료
            answer.append(food)

    # 섬이 하나도 없다면
    if not answer:
        return [-1]

    return sorted(answer)