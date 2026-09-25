from itertools import combinations

def solution(n, q, ans):
    answer = 0

    # 1 ~ n 중 5개를 선택하는 모든 조합
    for code in combinations(range(1, n + 1), 5):

        # 모든 시도의 조건을 만족하는지 확인
        for i in range(len(q)):
            count = 0

            # 현재 후보 코드와 q[i]에서 겹치는 숫자 개수
            for num in q[i]:
                if num in code:
                    count += 1

            # 시스템 응답과 다르면 이 후보는 탈락
            if count != ans[i]:
                break

        else:
            # 모든 시도를 통과한 경우
            answer += 1

    return answer