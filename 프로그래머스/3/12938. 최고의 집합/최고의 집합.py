def solution(n, s):
    if n > s:
        return [-1]

    a, b = divmod(s, n)

    answer = [a] * (n - b) + [a + 1] * b

    return answer