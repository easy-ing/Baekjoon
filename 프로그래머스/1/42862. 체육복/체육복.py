def solution(n, lost, reserve):
    # 도난당했지만 여벌도 있는 학생 제외
    real_lost = sorted(set(lost) - set(reserve))
    real_reserve = set(reserve) - set(lost)

    # 체육복이 없는 학생에게 앞번호부터 빌려주기
    for student in real_lost:
        if student - 1 in real_reserve:
            real_reserve.remove(student - 1)
        elif student + 1 in real_reserve:
            real_reserve.remove(student + 1)
        else:
            n -= 1

    return n