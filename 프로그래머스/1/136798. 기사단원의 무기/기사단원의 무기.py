def solution(number, limit, power):
    answer = 0

    for knight in range(1, number + 1):
        divisor_count = 0

        for i in range(1, int(knight ** 0.5) + 1):
            if knight % i == 0:
                divisor_count += 1

                if i != knight // i:
                    divisor_count += 1

        if divisor_count > limit:
            answer += power
        else:
            answer += divisor_count

    return answer