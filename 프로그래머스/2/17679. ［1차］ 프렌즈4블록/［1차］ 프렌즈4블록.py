def solution(m, n, board):
    # 문자열은 수정할 수 없으므로 리스트로 변환
    board = [list(row) for row in board]

    answer = 0

    while True:
        remove = set()

        # 1. 삭제할 블록 찾기
        for r in range(m - 1):
            for c in range(n - 1):
                if board[r][c] == ' ':
                    continue

                if (
                    board[r][c] == board[r + 1][c] ==
                    board[r][c + 1] == board[r + 1][c + 1]
                ):
                    remove.add((r, c))
                    remove.add((r + 1, c))
                    remove.add((r, c + 1))
                    remove.add((r + 1, c + 1))

        # 삭제할 블록이 없다면 종료
        if not remove:
            break

        # 2. 블록 삭제
        answer += len(remove)

        for r, c in remove:
            board[r][c] = ' '

        # 3. 블록 떨어뜨리기
        for c in range(n):
            blocks = []

            # 현재 열에서 살아있는 블록만 모으기
            for r in range(m):
                if board[r][c] != ' ':
                    blocks.append(board[r][c])

            # 위쪽은 빈칸
            empty = m - len(blocks)

            for r in range(empty):
                board[r][c] = ' '

            # 아래쪽에 블록 채우기
            for r in range(empty, m):
                board[r][c] = blocks[r - empty]

    return answer