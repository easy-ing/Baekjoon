import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    arr = [0] * M
    out = []

    def dfs(depth, start):
        if depth == M:
            out.append(" ".join(map(str, arr)))
            return
        for x in range(start, N + 1):   # start부터 시작 -> 비내림차순 유지
            arr[depth] = x
            dfs(depth + 1, x)           # 다음도 x 이상만 선택 가능

    dfs(0, 1)
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()