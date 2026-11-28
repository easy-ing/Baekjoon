def solution(a):
    answer = 0

    left_min = float('inf')
    right_min = float('inf')

    # 왼쪽에서부터 최솟값 확인
    for num in a:
        if num < left_min:
            answer += 1
            left_min = num

    # 오른쪽에서부터 최솟값 확인
    for num in reversed(a):
        if num < right_min:
            answer += 1
            right_min = num

    # 양쪽 최솟값으로 중복 계산된 최솟값 제거
    answer -= 1

    return answer