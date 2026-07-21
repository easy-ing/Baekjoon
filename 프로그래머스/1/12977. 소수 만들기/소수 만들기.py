from itertools import combinations


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def solution(nums):
    answer = 0

    for numbers in combinations(nums, 3):
        total = sum(numbers)

        if is_prime(total):
            answer += 1

    return answer