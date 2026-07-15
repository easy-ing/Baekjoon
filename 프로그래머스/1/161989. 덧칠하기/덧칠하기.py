def solution(n, m, section):
    answer = 0
    painted_until = 0

    for area in section:
        if area > painted_until:
            answer += 1
            painted_until = area + m - 1

    return answer