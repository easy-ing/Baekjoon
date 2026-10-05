def solution(board):
    def win(player):
        # 가로
        for row in board:
            if row == player * 3:
                return True

        # 세로
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True

        # 대각선
        if all(board[i][i] == player for i in range(3)):
            return True

        if all(board[i][2 - i] == player for i in range(3)):
            return True

        return False

    o_count = sum(row.count("O") for row in board)
    x_count = sum(row.count("X") for row in board)

    # O가 X보다 1개 이상 많거나, X가 O보다 많으면 불가능
    if o_count < x_count or o_count > x_count + 1:
        return 0

    o_win = win("O")
    x_win = win("X")

    # 둘 다 승리하는 것은 불가능
    if o_win and x_win:
        return 0

    # O가 이겼다면 O가 마지막으로 둔 상황이어야 함
    if o_win:
        return 1 if o_count == x_count + 1 else 0

    # X가 이겼다면 X가 마지막으로 둔 상황이어야 함
    if x_win:
        return 1 if o_count == x_count else 0

    # 승자가 없다면 정상적인 턴 수만 맞으면 됨
    return 1