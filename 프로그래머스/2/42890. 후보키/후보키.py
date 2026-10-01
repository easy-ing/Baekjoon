from itertools import combinations

def solution(relation):
    n = len(relation)       # 행 개수
    m = len(relation[0])    # 컬럼 개수

    candidate_keys = []

    # 1개 컬럼부터 m개 컬럼까지 조합을 만든다.
    for size in range(1, m + 1):
        for columns in combinations(range(m), size):

            # -------------------------
            # 최소성 검사
            # -------------------------
            # 현재 조합 안에 이미 후보키가 있다면
            # 현재 조합은 최소성을 만족하지 못한다.
            is_minimal = True

            for key in candidate_keys:
                if set(key).issubset(columns):
                    is_minimal = False
                    break

            if not is_minimal:
                continue

            # -------------------------
            # 유일성 검사
            # -------------------------
            values = set()

            for row in relation:
                value = tuple(row[col] for col in columns)
                values.add(value)

            # 모든 행이 서로 다르다면 유일성 만족
            if len(values) == n:
                candidate_keys.append(columns)

    return len(candidate_keys)