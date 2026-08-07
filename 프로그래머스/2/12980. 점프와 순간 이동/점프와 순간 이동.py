def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            # 순간이동: 배터리 사용량 0
            n //= 2
        else:
            # 홀수는 점프를 한 번 해야 함
            n -= 1
            ans += 1
    return ans