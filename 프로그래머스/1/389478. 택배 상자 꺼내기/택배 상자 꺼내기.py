def solution(n, w, num):
    # num의 층과 열
    row = (num - 1) // w
    pos = (num - 1) % w

    if row % 2 == 0:
        col = pos
    else:
        col = w - 1 - pos

    answer = 1  # 자기 자신

    max_row = (n - 1) // w

    for r in range(row + 1, max_row + 1):
        if r % 2 == 0:
            idx = r * w + col + 1
        else:
            idx = r * w + (w - col)

        if idx <= n:
            answer += 1

    return answer