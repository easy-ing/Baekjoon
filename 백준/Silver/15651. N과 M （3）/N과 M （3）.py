import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    arr = [0] * M
    out = []

    def dfs(depth):
        if depth == M:
            out.append(" ".join(map(str, arr)))
            return
        for x in range(1, N + 1):
            arr[depth] = x
            dfs(depth + 1)

    dfs(0)
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()