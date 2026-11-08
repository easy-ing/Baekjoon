def solution(gems):
    total = len(set(gems))

    gems_count = {}
    left = 0

    best = [0, len(gems) - 1]

    for right in range(len(gems)):
        # 오른쪽 보석 추가
        gem = gems[right]
        gems_count[gem] = gems_count.get(gem, 0) + 1

        # 모든 종류의 보석이 포함되었다면
        while len(gems_count) == total:

            # 현재 구간이 더 짧거나 시작 번호가 더 작은 경우
            if right - left < best[1] - best[0]:
                best = [left, right]

            # 왼쪽 보석 제거
            left_gem = gems[left]
            gems_count[left_gem] -= 1

            # 해당 보석이 더 이상 구간에 없다면 삭제
            if gems_count[left_gem] == 0:
                del gems_count[left_gem]

            left += 1

    # 진열대 번호는 1번부터 시작
    return [best[0] + 1, best[1] + 1]