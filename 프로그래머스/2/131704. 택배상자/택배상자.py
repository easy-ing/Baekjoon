def solution(order):
    stack = []
    answer = 0
    box = 1

    for target in order:
        # 기존 컨테이너 벨트에서 target이 나올 때까지
        # 상자를 보조 컨테이너 벨트(스택)에 넣는다.
        while box <= len(order) and box < target:
            stack.append(box)
            box += 1

        # 기존 컨테이너 벨트에서 바로 target을 꺼낼 수 있는 경우
        if box == target:
            answer += 1
            box += 1

        # 스택의 맨 위가 target인 경우
        elif stack and stack[-1] == target:
            stack.pop()
            answer += 1

        # 어느 곳에서도 target을 꺼낼 수 없는 경우
        else:
            break

    return answer