from collections import deque


def solution(places):
    answer = []

    # 상, 하, 좌, 우
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for place in places:
        is_valid = True

        # 모든 응시자에서 BFS 시작
        for r in range(5):
            for c in range(5):
                if place[r][c] != 'P':
                    continue

                queue = deque()
                queue.append((r, c, 0))

                visited = [[False] * 5 for _ in range(5)]
                visited[r][c] = True

                while queue:
                    cr, cc, distance = queue.popleft()

                    # 거리 2까지만 확인
                    if distance == 2:
                        continue

                    for dr, dc in directions:
                        nr = cr + dr
                        nc = cc + dc
                        next_distance = distance + 1

                        # 대기실 범위를 벗어나면 무시
                        if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
                            continue

                        # 이미 방문한 곳이면 무시
                        if visited[nr][nc]:
                            continue

                        # 파티션이면 통과할 수 없음
                        if place[nr][nc] == 'X':
                            continue

                        # 다른 응시자를 만났다면 거리두기 위반
                        if place[nr][nc] == 'P':
                            is_valid = False
                            break

                        visited[nr][nc] = True
                        queue.append((nr, nc, next_distance))

                    if not is_valid:
                        break

                if not is_valid:
                    break

            if not is_valid:
                break

        answer.append(1 if is_valid else 0)

    return answer