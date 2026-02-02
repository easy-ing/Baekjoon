import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = []
out = []

def dfs(start: int):
    if len(seq) == M:
        out.append(' '.join(map(str, seq)))
        return
    for x in range(start, N + 1):
        seq.append(x)
        dfs(x + 1)
        seq.pop()

dfs(1)
sys.stdout.write('\n'.join(out))