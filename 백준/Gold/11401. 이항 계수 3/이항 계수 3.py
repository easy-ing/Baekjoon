import sys
input = sys.stdin.readline

MOD = 1000000007

n, k = map(int, input().split())

# n! 계산
fact = [1] * (n + 1)
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % MOD

# 분모 = k! * (n-k)!
denominator = fact[k] * fact[n - k] % MOD

# 페르마의 소정리로 역원 구하기
answer = fact[n] * pow(denominator, MOD - 2, MOD) % MOD

print(answer)