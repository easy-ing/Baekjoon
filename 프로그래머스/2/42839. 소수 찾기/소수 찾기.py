def solution(numbers):
    answer = set()

    def is_prime(num):
        if num < 2:
            return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True

    def dfs(current, remaining):
        # 현재까지 만든 숫자가 소수인지 확인
        if current:
            num = int(current)

            if is_prime(num):
                answer.add(num)

        # 남은 숫자를 하나씩 붙여보기
        for i in range(len(remaining)):
            dfs(
                current + remaining[i],
                remaining[:i] + remaining[i + 1:]
            )

    dfs("", numbers)

    return len(answer)