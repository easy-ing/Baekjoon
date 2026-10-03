def solution(n):
    answer = 0
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    def backtracking(row):
        nonlocal answer

        # 모든 행에 퀸을 배치했다면 하나의 경우 완성
        if row == n:
            answer += 1
            return

        for col in range(n):
            # 같은 열에 퀸이 있는 경우
            if cols[col]:
                continue

            # / 대각선
            if diag1[row + col]:
                continue

            # \ 대각선
            if diag2[row - col + n - 1]:
                continue

            # 퀸 배치
            cols[col] = True
            diag1[row + col] = True
            diag2[row - col + n - 1] = True

            backtracking(row + 1)

            # 퀸 제거
            cols[col] = False
            diag1[row + col] = False
            diag2[row - col + n - 1] = False

    backtracking(0)

    return answer