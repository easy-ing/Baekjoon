def solution(players, callings):
    # 선수 이름별 현재 등수 저장
    rank = {
        player: index
        for index, player in enumerate(players)
    }

    for called_player in callings:
        current_rank = rank[called_player]
        front_player = players[current_rank - 1]

        # 두 선수의 위치 교환
        players[current_rank - 1], players[current_rank] = (
            players[current_rank],
            players[current_rank - 1]
        )

        # 변경된 등수 갱신
        rank[called_player] -= 1
        rank[front_player] += 1

    return players