def solution(elements):
    n = len(elements)
    # 원형 수열을 선형으로 만들기 위해 2배로 확장
    elements *= 2
    # 중복을 제거하기 위한 집합
    sums = set()
    # 길이 1 ~ n인 모든 연속 부분 수열
    for length in range(1, n + 1):
        current_sum = sum(elements[:length])
        sums.add(current_sum)
        # 시작 위치를 한 칸씩 이동
        for start in range(1, n):
            current_sum += elements[start + length - 1]
            current_sum -= elements[start - 1]
            sums.add(current_sum)
    return len(sums)