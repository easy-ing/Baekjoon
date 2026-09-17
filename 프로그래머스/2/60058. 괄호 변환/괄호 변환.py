def solution(p):
    # 1. 빈 문자열이면 그대로 반환
    if not p:
        return ''

    # 2. 가장 짧은 균형잡힌 문자열 u, 나머지 v로 분리
    count = 0

    for i, char in enumerate(p):
        if char == '(':
            count += 1
        else:
            count -= 1

        # 처음으로 균형이 맞는 지점
        if count == 0:
            u = p[:i + 1]
            v = p[i + 1:]
            break

    # 3. u가 올바른 괄호 문자열인지 확인
    count = 0
    correct = True

    for char in u:
        if char == '(':
            count += 1
        else:
            count -= 1

        # 닫는 괄호가 더 많아지는 순간 잘못된 문자열
        if count < 0:
            correct = False
            break

    # u가 올바른 괄호 문자열이면
    if correct:
        return u + solution(v)

    # 4. u가 올바르지 않은 경우
    # u의 첫 번째와 마지막 문자를 제거
    middle = u[1:-1]

    # 괄호 방향 뒤집기
    flipped = ''
    for char in middle:
        if char == '(':
            flipped += ')'
        else:
            flipped += '('

    # "(" + v를 변환한 결과 + ")" + 뒤집은 문자열
    return '(' + solution(v) + ')' + flipped