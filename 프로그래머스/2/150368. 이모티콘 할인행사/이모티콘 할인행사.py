def solution(users, emoticons):
    answer = [0, 0]
    discounts = [10, 20, 30, 40]

    def dfs(index, selected):
        # 모든 이모티콘의 할인율을 정했다면 계산
        if index == len(emoticons):
            plus = 0
            sales = 0

            for rate, limit in users:
                total = 0

                for i in range(len(emoticons)):
                    # 사용자의 기준 할인율 이상이면 구매
                    if selected[i] >= rate:
                        price = emoticons[i] * (100 - selected[i]) // 100
                        total += price

                # 구매 금액이 기준 이상이면 플러스 가입
                if total >= limit:
                    plus += 1
                else:
                    sales += total

            # 가입자 수가 우선, 매출이 다음
            if plus > answer[0]:
                answer[0] = plus
                answer[1] = sales
            elif plus == answer[0] and sales > answer[1]:
                answer[1] = sales

            return

        # 현재 이모티콘에 10/20/30/40% 할인 적용
        for discount in discounts:
            selected.append(discount)
            dfs(index + 1, selected)
            selected.pop()

    dfs(0, [])

    return answer