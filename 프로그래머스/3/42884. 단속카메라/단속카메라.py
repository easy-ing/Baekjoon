def solution(routes):
    routes.sort(key=lambda x: x[1])

    answer = 0
    camera = float('-inf')

    for start, end in routes:
        if start > camera:
            camera = end
            answer += 1

    return answer