from collections import Counter


def solution(topping):
    # 처음에는 모든 토핑이 오른쪽에 있다.
    right = Counter(topping)

    # 왼쪽에 존재하는 토핑 종류
    left = set()

    answer = 0

    for t in topping:
        # 토핑 하나를 왼쪽으로 이동
        left.add(t)

        # 오른쪽에서는 하나 제거
        right[t] -= 1

        # 해당 토핑이 오른쪽에 더 이상 없다면
        # 오른쪽 토핑 종류에서도 제거
        if right[t] == 0:
            del right[t]

        # 양쪽 토핑 종류의 개수가 같으면 공평한 경우
        if len(left) == len(right):
            answer += 1

    return answer