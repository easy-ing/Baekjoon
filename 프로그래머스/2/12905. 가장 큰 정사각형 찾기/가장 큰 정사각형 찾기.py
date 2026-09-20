def solution(board):
    rows = len(board)
    cols = len(board[0])

    max_side = 0

    for i in range(rows):
        for j in range(cols):
            # 현재 칸이 0이면 정사각형을 만들 수 없음
            if board[i][j] == 0:
                continue

            # 첫 번째 행/열은 이전 칸을 볼 수 없음
            if i == 0 or j == 0:
                board[i][j] = 1
            else:
                board[i][j] = min(
                    board[i - 1][j],      # 위
                    board[i][j - 1],      # 왼쪽
                    board[i - 1][j - 1]  # 왼쪽 위
                ) + 1

            max_side = max(max_side, board[i][j])

    return max_side ** 2