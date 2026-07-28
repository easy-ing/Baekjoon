def solution(schedules, timelogs, startday):
    answer = 0

    for schedule, timelog in zip(schedules, timelogs):
        hour = schedule // 100
        minute = schedule % 100 + 10

        # 10분을 더했을 때 60분 이상이면 다음 시간으로 넘김
        if minute >= 60:
            hour += 1
            minute -= 60

        limit_time = hour * 100 + minute
        is_success = True

        for day in range(7):
            weekday = (startday - 1 + day) % 7 + 1

            # 토요일과 일요일은 검사하지 않음
            if weekday == 6 or weekday == 7:
                continue

            if timelog[day] > limit_time:
                is_success = False
                break

        if is_success:
            answer += 1

    return answer