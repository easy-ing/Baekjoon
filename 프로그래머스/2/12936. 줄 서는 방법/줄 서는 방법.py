def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))

    for i in range(n, 0, -1):
        factorial = 1

        # (i - 1)!
        for j in range(1, i):
            factorial *= j

        # k는 1부터 시작하므로 0-based로 변환
        index = (k - 1) // factorial

        answer.append(numbers.pop(index))

        # 다음 그룹에서의 순서
        k = (k - 1) % factorial + 1

    return answer