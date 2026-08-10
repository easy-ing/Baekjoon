def solution(clothes):
    clothes_count = {}

    # 의상 종류별 개수 세기
    for name, category in clothes:
        clothes_count[category] = clothes_count.get(category, 0) + 1

    answer = 1

    # 각 종류마다 "안 입기"를 포함해서 경우의 수 계산
    for count in clothes_count.values():
        answer *= count + 1

    # 아무것도 입지 않는 경우 제외
    return answer - 1