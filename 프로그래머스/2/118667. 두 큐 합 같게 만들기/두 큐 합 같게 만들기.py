def solution(queue1, queue2):
    n = len(queue1)

    total = sum(queue1) + sum(queue2)

    # 전체 합이 홀수면 절대 같게 만들 수 없음
    if total % 2:
        return -1

    target = total // 2

    # 두 큐를 이어 붙임
    arr = queue1 + queue2

    left = 0
    right = n
    current = sum(queue1)

    answer = 0

    # 각 포인터가 최대 2n 정도 이동하면 충분
    while left < 2 * n and right < 2 * n:
        if current == target:
            return answer

        if current < target:
            current += arr[right]
            right += 1
            answer += 1

        else:
            current -= arr[left]
            left += 1
            answer += 1

    return -1