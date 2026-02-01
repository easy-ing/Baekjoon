import sys
input = sys.stdin.readline

N, M = map(int, input().split())
used = [False] * (N + 1)
seq = []
out = []

def dfs(depth: int):
    if depth == M:
        out.append(' '.join(map(str, seq)))
        return
    for x in range(1, N + 1):
        if not used[x]:
            used[x] = True
            seq.append(x)
            dfs(depth + 1)
            seq.pop()
            used[x] = False

dfs(0)
sys.stdout.write('\n'.join(out))