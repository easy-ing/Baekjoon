def solution(arr):
    answer = [0, 0]

    def divide(x, y, size):
        # 현재 영역의 첫 번째 값
        value = arr[x][y]

        # 현재 영역이 모두 같은 값인지 확인
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != value:
                    # 값이 섞여 있다면 4등분
                    half = size // 2

                    divide(x, y, half)                  # 왼쪽 위
                    divide(x, y + half, half)           # 오른쪽 위
                    divide(x + half, y, half)           # 왼쪽 아래
                    divide(x + half, y + half, half)    # 오른쪽 아래

                    return

        # 현재 영역이 모두 같은 값
        answer[value] += 1

    divide(0, 0, len(arr))

    return answer