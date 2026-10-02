def solution(k, d):
    answer = 0
    max_y = d // k

    for x in range(0, d + 1, k):
        # x² + y² <= d²를 만족하는 최대 y
        while (x * x + (max_y * k) ** 2) > d * d:
            max_y -= 1

        # y = 0, k, 2k, ..., max_y*k
        answer += max_y + 1

    return answer