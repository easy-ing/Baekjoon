from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for size in course:
        counter = Counter()

        for order in orders:
            # 주문을 알파벳순으로 정렬
            order = sorted(order)

            # size개짜리 조합 생성
            for combination in combinations(order, size):
                menu = ''.join(combination)
                counter[menu] += 1

        # 해당 코스 크기에서 가장 많이 주문된 횟수
        if counter:
            max_count = max(counter.values())

            # 최소 2명 이상 주문된 경우만
            if max_count >= 2:
                for menu, count in counter.items():
                    if count == max_count:
                        answer.append(menu)

    # 전체 메뉴를 사전순 정렬
    answer.sort()

    return answer