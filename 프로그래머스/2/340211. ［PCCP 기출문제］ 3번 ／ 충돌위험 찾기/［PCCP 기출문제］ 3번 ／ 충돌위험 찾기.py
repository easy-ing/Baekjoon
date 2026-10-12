def solution(points, routes):
    answer = 0
    robot_paths = []

    for route in routes:
        path = []

        r, c = points[route[0] - 1]
        path.append((r, c))

        for i in range(1, len(route)):
            nr, nc = points[route[i] - 1]

            while r != nr:
                r += 1 if nr > r else -1
                path.append((r, c))

            while c != nc:
                c += 1 if nc > c else -1
                path.append((r, c))

        robot_paths.append(path)

    max_time = max(len(path) for path in robot_paths)

    for t in range(max_time):
        positions = {}

        for path in robot_paths:
            if t < len(path):
                pos = path[t]
                positions[pos] = positions.get(pos, 0) + 1

        for count in positions.values():
            if count >= 2:
                answer += 1

    return answer