def solution(X, Y):
    answer = []

    for number in range(9, -1, -1):
        count = min(X.count(str(number)), Y.count(str(number)))
        answer.append(str(number) * count)

    result = ''.join(answer)

    if result == '':
        return '-1'

    if result[0] == '0':
        return '0'

    return result