def solution(grid):
    answer = []

    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (-1, 0),  # 위
        (0, 1),   # 오른쪽
        (1, 0),   # 아래
        (0, -1)   # 왼쪽
    ]

    visited = [[[False] * 4 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            for d in range(4):
                if not visited[r][c][d]:
                    count = 0

                    while not visited[r][c][d]:
                        visited[r][c][d] = True
                        count += 1

                        if grid[r][c] == "L":
                            d = (d - 1) % 4
                        elif grid[r][c] == "R":
                            d = (d + 1) % 4

                        r = (r + directions[d][0]) % rows
                        c = (c + directions[d][1]) % cols

                    answer.append(count)

    answer.sort()
    return answer