def solution(keymap, targets):
    press_count = {}

    # 각 문자별 최소 입력 횟수 저장
    for key in keymap:
        for i, char in enumerate(key):
            count = i + 1

            if char not in press_count:
                press_count[char] = count
            else:
                press_count[char] = min(press_count[char], count)

    answer = []

    # target별로 필요한 입력 횟수 계산
    for target in targets:
        total = 0

        for char in target:
            if char not in press_count:
                total = -1
                break

            total += press_count[char]

        answer.append(total)

    return answer