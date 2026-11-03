def solution(n, stations, w):
    answer = 0
    position = 1

    # 기지국 하나가 커버할 수 있는 아파트 수
    coverage = 2 * w + 1

    for station in stations:
        # 기존 기지국의 전파가 도달하기 전까지의 구간
        left = station - w

        # 전파가 닿지 않는 아파트 수
        uncovered = left - position

        if uncovered > 0:
            # 필요한 최소 기지국 수
            answer += (uncovered + coverage - 1) // coverage

        # 기존 기지국이 커버하는 구간 다음 아파트로 이동
        position = station + w + 1

    # 마지막 기존 기지국 이후의 남은 구간
    if position <= n:
        uncovered = n - position + 1
        answer += (uncovered + coverage - 1) // coverage

    return answer