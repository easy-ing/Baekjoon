def solution(rows, columns, queries):
    matrix = [
        [r * columns + c + 1 for c in range(columns)]
        for r in range(rows)
    ]

    answer = []

    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        # 왼쪽 위 값을 임시 저장
        temp = matrix[x1][y1]
        min_value = temp

        # 1. 왼쪽 열
        # 아래 -> 위로 한 칸씩 이동
        for x in range(x1, x2):
            matrix[x][y1] = matrix[x + 1][y1]
            min_value = min(min_value, matrix[x][y1])

        # 2. 아래쪽 행
        # 왼쪽 -> 오른쪽
        for y in range(y1, y2):
            matrix[x2][y] = matrix[x2][y + 1]
            min_value = min(min_value, matrix[x2][y])

        # 3. 오른쪽 열
        # 아래 -> 위
        for x in range(x2, x1, -1):
            matrix[x][y2] = matrix[x - 1][y2]
            min_value = min(min_value, matrix[x][y2])

        # 4. 위쪽 행
        # 오른쪽 -> 왼쪽
        for y in range(y2, y1, -1):
            matrix[x1][y] = matrix[x1][y - 1]
            min_value = min(min_value, matrix[x1][y])

        # 원래 왼쪽 위 값을 위쪽 행의 두 번째 위치에 넣음
        matrix[x1][y1 + 1] = temp

        answer.append(min_value)

    return answer