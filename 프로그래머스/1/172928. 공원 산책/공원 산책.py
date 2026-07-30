def solution(park, routes):
    h = len(park)
    w = len(park[0])

    # 시작 위치 찾기
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                r, c = i, j
                break

    # 방향
    direction = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }

    for route in routes:
        op, dist = route.split()
        dist = int(dist)

        dr, dc = direction[op]

        nr, nc = r, c
        possible = True

        # 이동 경로 검사
        for _ in range(dist):
            nr += dr
            nc += dc

            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                possible = False
                break

            if park[nr][nc] == "X":
                possible = False
                break

        # 가능하면 이동
        if possible:
            r, c = nr, nc

    return [r, c]