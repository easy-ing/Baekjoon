def solution(n):
    digits = list(str(n))      # 숫자를 문자열로 바꿔 자릿수 분리
    digits.sort(reverse=True)  # 큰 숫자부터 정렬
    return int(''.join(digits))