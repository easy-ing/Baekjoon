def solution(n):
    answer = [[0] * n for _ in range(n)]

    x, y = -1, 0
    num = 1

    directions = [(1, 0), (0, 1), (-1, -1)]

    for size in range(n, 0, -1):
        dx, dy = directions[(n - size) % 3]

        for _ in range(size):
            x += dx
            y += dy
            answer[x][y] = num
            num += 1

    return [num for row in answer for num in row if num != 0]