import math

def solution(fees, records):
    answer = []

    base_time, base_fee, unit_time, unit_fee = fees

    in_time = {}
    total_time = {}

    def to_minutes(time):
        hour, minute = time.split(":")
        return int(hour) * 60 + int(minute)

    for record in records:
        time, car, status = record.split()
        minute = to_minutes(time)

        if status == "IN":
            in_time[car] = minute

        else:
            parked_time = minute - in_time[car]

            if car not in total_time:
                total_time[car] = 0

            total_time[car] += parked_time

            del in_time[car]

    end_time = to_minutes("23:59")

    for car in in_time:
        parked_time = end_time - in_time[car]

        if car not in total_time:
            total_time[car] = 0

        total_time[car] += parked_time

    for car in sorted(total_time.keys()):
        time = total_time[car]

        if time <= base_time:
            answer.append(base_fee)
        else:
            extra_time = time - base_time
            extra_fee = math.ceil(extra_time / unit_time) * unit_fee
            answer.append(base_fee + extra_fee)

    return answer