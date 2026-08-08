def solution(want, number, discount):
    answer = 0

    # 정현이가 원하는 상품과 수량
    want_count = dict(zip(want, number))

    # 처음 10일의 할인 상품 개수
    current = {}

    for i in range(10):
        current[discount[i]] = current.get(discount[i], 0) + 1

    # 현재 10일이 원하는 조건과 일치하는지 확인
    if current == want_count:
        answer += 1

    # 10일 윈도우를 한 칸씩 이동
    for i in range(10, len(discount)):
        # 윈도우에서 빠지는 상품
        remove_item = discount[i - 10]
        current[remove_item] -= 1

        # 윈도우에서 개수가 0이 된 상품 제거
        if current[remove_item] == 0:
            del current[remove_item]

        # 새롭게 들어오는 상품
        add_item = discount[i]
        current[add_item] = current.get(add_item, 0) + 1

        # 원하는 상품 및 수량과 정확히 일치하는지 확인
        if current == want_count:
            answer += 1

    return answer