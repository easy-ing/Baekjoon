def solution(sequence):
    answer = 0

    dp1 = 0
    dp2 = 0

    for i in range(len(sequence)):
        num1 = sequence[i] * (1 if i % 2 == 0 else -1)
        num2 = sequence[i] * (-1 if i % 2 == 0 else 1)

        dp1 = max(num1, dp1 + num1)
        dp2 = max(num2, dp2 + num2)

        answer = max(answer, dp1, dp2)

    return answer