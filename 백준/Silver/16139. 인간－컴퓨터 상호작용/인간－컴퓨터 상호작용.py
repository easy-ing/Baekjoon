import sys

input = sys.stdin.readline

# 문자열 입력
S = input().strip()
n = len(S)

# 알파벳 26개에 대한 누적합 배열
# prefix[i][c] : S의 앞에서부터 i개 문자까지 봤을 때 c의 등장 횟수
prefix = [[0] * 26 for _ in range(n + 1)]

for i in range(n):
    # 이전 값 복사
    for c in range(26):
        prefix[i + 1][c] = prefix[i][c]
    # 현재 문자 반영
    prefix[i + 1][ord(S[i]) - ord('a')] += 1

q = int(input())
answers = []

for _ in range(q):
    alpha, l, r = input().split()
    l = int(l)
    r = int(r)

    idx = ord(alpha) - ord('a')
    count = prefix[r + 1][idx] - prefix[l][idx]
    answers.append(str(count))

print('\n'.join(answers))