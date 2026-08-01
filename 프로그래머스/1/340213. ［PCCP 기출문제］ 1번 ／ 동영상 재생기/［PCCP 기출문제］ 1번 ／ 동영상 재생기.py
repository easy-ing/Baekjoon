def solution(video_len, pos, op_start, op_end, commands):

    def to_second(time):
        m, s = map(int, time.split(":"))
        return m * 60 + s

    def to_time(sec):
        return f"{sec // 60:02d}:{sec % 60:02d}"

    video_len = to_second(video_len)
    pos = to_second(pos)
    op_start = to_second(op_start)
    op_end = to_second(op_end)

    def skip_opening(pos):
        if op_start <= pos <= op_end:
            return op_end
        return pos

    # 시작 위치에서도 오프닝 여부 확인
    pos = skip_opening(pos)

    for command in commands:
        if command == "prev":
            pos = max(0, pos - 10)
        else:
            pos = min(video_len, pos + 10)

        # 명령 수행 후 오프닝 여부 확인
        pos = skip_opening(pos)

    return to_time(pos)