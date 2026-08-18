def solution(n, t, m, p):
    digits = "0123456789ABCDEF"

    def convert(num):
        if num == 0:
            return "0"

        result = ""

        while num > 0:
            result = digits[num % n] + result
            num //= n

        return result

    numbers = ""
    num = 0

    while len(numbers) < t * m:
        numbers += convert(num)
        num += 1

    answer = ""

    for i in range(t):
        answer += numbers[p - 1 + i * m]

    return answer