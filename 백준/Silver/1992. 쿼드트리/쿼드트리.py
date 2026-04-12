import sys
input = sys.stdin.readline

n = int(input())
board = [input().strip() for _ in range(n)]

def quad(x, y, size):
    first = board[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if board[i][j] != first:
                half = size // 2
                return (
                    "("
                    + quad(x, y, half)
                    + quad(x, y + half, half)
                    + quad(x + half, y, half)
                    + quad(x + half, y + half, half)
                    + ")"
                )

    return first

print(quad(0, 0, n))