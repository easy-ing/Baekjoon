def solution(friends, gifts):
    n = len(friends)

    idx = {name: i for i, name in enumerate(friends)}

    give = [[0] * n for _ in range(n)]
    send = [0] * n
    receive = [0] * n

    for gift in gifts:
        a, b = gift.split()
        a = idx[a]
        b = idx[b]

        give[a][b] += 1
        send[a] += 1
        receive[b] += 1

    score = [send[i] - receive[i] for i in range(n)]

    next_receive = [0] * n

    for i in range(n):
        for j in range(i + 1, n):

            if give[i][j] > give[j][i]:
                next_receive[i] += 1

            elif give[i][j] < give[j][i]:
                next_receive[j] += 1

            else:
                if score[i] > score[j]:
                    next_receive[i] += 1
                elif score[i] < score[j]:
                    next_receive[j] += 1

    return max(next_receive)