def solution(a, b):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total = b - 1

    for i in range(a - 1):
        total += month[i]

    return days[total % 7]