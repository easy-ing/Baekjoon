from itertools import combinations

def solution(nums):
    answer = 0

    for numbers in combinations(nums, 3):
        total = sum(numbers)

        if is_prime(total):
            answer += 1

    return answer


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True