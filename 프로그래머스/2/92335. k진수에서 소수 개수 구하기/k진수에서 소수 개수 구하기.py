import math

def solution(n, k):
    # k진수 변환
    def convert(num):
        if num == 0:
            return "0"

        result = ""
        while num > 0:
            result = str(num % k) + result
            num //= k

        return result

    # 소수 판별
    def is_prime(num):
        if num < 2:
            return False

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False

        return True

    converted = convert(n)

    answer = 0

    for num in converted.split("0"):
        if num and is_prime(int(num)):
            answer += 1

    return answer