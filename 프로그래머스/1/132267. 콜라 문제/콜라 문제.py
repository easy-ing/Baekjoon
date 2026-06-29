def solution(a, b, n):
    answer = 0

    while n >= a:
        coke = (n // a) * b
        remain = n % a

        answer += coke
        n = remain + coke

    return answer