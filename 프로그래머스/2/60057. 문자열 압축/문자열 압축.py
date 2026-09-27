def solution(s):
    answer = len(s)

    # 자르는 단위: 1개 ~ 문자열의 절반
    for unit in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[:unit]
        count = 1

        # unit 단위로 문자열 탐색
        for i in range(unit, len(s), unit):
            current = s[i:i + unit]

            if current == prev:
                count += 1
            else:
                # 이전 문자열 압축
                if count == 1:
                    compressed += prev
                else:
                    compressed += str(count) + prev

                prev = current
                count = 1

        # 마지막 문자열 처리
        if count == 1:
            compressed += prev
        else:
            compressed += str(count) + prev

        # 압축 결과 중 가장 짧은 길이
        answer = min(answer, len(compressed))

    return answer