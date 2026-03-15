n = int(input())

# 피보나치 계산
f = [0] * (n + 1)
f[1] = f[2] = 1

for i in range(3, n + 1):
    f[i] = f[i-1] + f[i-2]

code1 = f[n]      # 재귀에서 코드1 실행 횟수
code2 = n - 2     # DP에서 코드2 실행 횟수

print(code1, code2)