def get_block(x):
    if x == 1:
        return 0

    best = 1                      # 소수면 1번 블록만 깔려 있어요
    i = 2
    while i * i <= x:
        if x % i == 0:            # i가 x의 약수라면
            if x // i <= 10_000_000:
                return x // i     # 큰 짝꿍이 정답
            best = i              # 큰 짝꿍이 너무 크면 작은 짝꿍을 기억
        i += 1
    return best


def solution(begin, end):
    answer = []
    for x in range(begin, end + 1):   # end까지 포함하려고 +1
        answer.append(get_block(x))
    return answer