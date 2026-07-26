def solution(board, moves):
    answer = 0
    basket = []

    for move in moves:
        col = move - 1  # moves는 1번부터 시작하므로 인덱스로 변환

        for row in range(len(board)):
            doll = board[row][col]

            if doll != 0:
                board[row][col] = 0  # 인형을 뽑았으므로 빈칸 처리

                if basket and basket[-1] == doll:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(doll)

                break

    return answer