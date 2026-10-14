def solution(line):
    pts = set()
    n = len(line)
    for i in range(n):
        A, B, E = line[i]
        for j in range(i + 1, n):
            C, D, F = line[j]
            den = A * D - B * C
            if den == 0:          # 평행 또는 일치
                continue
            xn = B * F - E * D
            yn = E * C - A * F
            if xn % den == 0 and yn % den == 0:   # 정수 교점만
                pts.add((xn // den, yn // den))

    xs = [x for x, _ in pts]
    ys = [y for _, y in pts]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)

    grid = [['.'] * (maxx - minx + 1) for _ in range(maxy - miny + 1)]
    for x, y in pts:
        grid[maxy - y][x - minx] = '*'   # y가 클수록 위쪽 행
    return [''.join(row) for row in grid]