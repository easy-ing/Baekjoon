def solution(id_list, report, k):
    report = set(report)

    reported_count = {user: 0 for user in id_list}
    reported_by_me = {user: [] for user in id_list}

    for r in report:
        reporter, reported = r.split()

        reported_count[reported] += 1
        reported_by_me[reporter].append(reported)

    answer = []

    for user in id_list:
        mail_count = 0

        for reported_user in reported_by_me[user]:
            if reported_count[reported_user] >= k:
                mail_count += 1

        answer.append(mail_count)

    return answer