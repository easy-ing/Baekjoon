def solution(data, col, row_begin, row_end):
    # 1. col 기준 오름차순
    #    값이 같으면 기본키(첫 번째 컬럼) 기준 내림차순
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    answer = 0

    # 2. row_begin ~ row_end 행 처리
    for i in range(row_begin, row_end + 1):
        # 3. 각 컬럼 값을 i로 나눈 나머지의 합
        s = sum(value % i for value in data[i - 1])

        # 4. XOR 누적
        answer ^= s

    return answer