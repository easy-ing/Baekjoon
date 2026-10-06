from math import isqrt


def solution(r1, r2):
    answer = 0

    for x in range(1, r2 + 1):
        # 바깥 원 안에서 가능한 최대 y
        max_y = isqrt(r2 * r2 - x * x)

        # 안쪽 원 밖에서 시작해야 하는 최소 y
        if x < r1:
            value = r1 * r1 - x * x
            min_y = isqrt(value)

            if min_y * min_y < value:
                min_y += 1
        else:
            min_y = 0

        # y = 0은 별도로 처리하므로 최소 1
        min_y = max(min_y, 1)

        if min_y <= max_y:
            answer += max_y - min_y + 1

    # x > 0, y > 0인 점은 4방향 대칭
    answer *= 4

    # x = 0인 y축 위의 점
    answer += (r2 - r1 + 1) * 2

    # y = 0인 x축 위의 점
    answer += (r2 - r1 + 1) * 2

    return answer