def solution(numbers):
    answer = []

    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            bit = 1

            while n & bit:
                bit <<= 1

            answer.append(n + bit - (bit >> 1))

    return answer