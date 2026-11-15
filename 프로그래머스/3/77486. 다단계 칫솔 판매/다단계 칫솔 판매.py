def solution(enroll, referral, seller, amount):
    # 1. 판매원별 추천인 정보
    parent = {}

    for name, ref in zip(enroll, referral):
        parent[name] = ref

    # 2. 판매원별 누적 수익
    profit = {name: 0 for name in enroll}

    # 3. 판매 내역 처리
    for name, cnt in zip(seller, amount):
        money = cnt * 100
        current = name

        # 4. 추천인을 따라 이익 분배
        while current != "-" and money > 0:

            # 추천인에게 전달할 금액
            tax = money // 10

            # 현재 판매원이 가져가는 금액
            profit[current] += money - tax

            # 1원 미만이면 분배 종료
            if tax == 0:
                break

            # 추천인에게 전달
            current = parent[current]
            money = tax

    # 5. enroll 순서대로 결과 반환
    return [profit[name] for name in enroll]