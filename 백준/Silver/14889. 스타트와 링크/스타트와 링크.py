import sys
from itertools import combinations

def team_score(team, W):
    s = 0
    m = len(team)
    for i in range(m):
        a = team[i]
        for j in range(i + 1, m):
            b = team[j]
            if a < b:
                s += W[a][b]
            else:
                s += W[b][a]
    return s

def solve():
    input = sys.stdin.readline
    N = int(input().strip())
    S = [list(map(int, input().split())) for _ in range(N)]

    # W[i][j] = Sij + Sji for i < j
    W = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            W[i][j] = S[i][j] + S[j][i]

    half = N // 2
    ans = float('inf')

    # 0번 사람을 스타트 팀에 고정해서 중복 제거
    for comb in combinations(range(1, N), half - 1):
        start = [0] + list(comb)
        start_set = set(start)
        link = [i for i in range(N) if i not in start_set]

        s_score = team_score(start, W)
        l_score = team_score(link, W)
        diff = abs(s_score - l_score)

        if diff < ans:
            ans = diff
            if ans == 0:
                break

    print(ans)

if __name__ == "__main__":
    solve()