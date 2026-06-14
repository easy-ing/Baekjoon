def solution(record):
    answer = []

    nickname = {}
    logs = []

    for r in record:
        data = r.split()
        action = data[0]
        uid = data[1]

        if action == "Enter":
            name = data[2]
            nickname[uid] = name
            logs.append((uid, "님이 들어왔습니다."))

        elif action == "Leave":
            logs.append((uid, "님이 나갔습니다."))

        elif action == "Change":
            name = data[2]
            nickname[uid] = name

    for uid, message in logs:
        answer.append(nickname[uid] + message)

    return answer