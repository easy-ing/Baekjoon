def solution(m, n, startX, startY, balls):
    answer = []
    for a, b in balls:
        candidates = []
        if not (b == startY and a < startX):   # 왼쪽 벽
            candidates.append((startX + a) ** 2 + (startY - b) ** 2)
        if not (b == startY and a > startX):   # 오른쪽 벽
            candidates.append((2 * m - a - startX) ** 2 + (startY - b) ** 2)
        if not (a == startX and b < startY):   # 아래 벽
            candidates.append((startX - a) ** 2 + (startY + b) ** 2)
        if not (a == startX and b > startY):   # 위 벽
            candidates.append((startX - a) ** 2 + (2 * n - b - startY) ** 2)
        answer.append(min(candidates))
    return answer