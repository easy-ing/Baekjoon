def solution(players, m, k):
    answer = 0

    # servers[i] = i시에 새롭게 증설한 서버 수
    servers = [0] * 24

    for i in range(24):
        # 현재 시간에 필요한 증설 서버 수
        required = players[i] // m

        # 현재 시간에 이미 운영 중인 서버
        # i-k+1 ~ i-1 시간에 증설된 서버
        start = max(0, i - k + 1)
        running = sum(servers[start:i])

        # 부족한 서버만 새롭게 증설
        additional = max(0, required - running)

        servers[i] = additional
        answer += additional

    return answer