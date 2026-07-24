def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    match_count = 0

    for number in lottos:
        if number in win_nums:
            match_count += 1

    best_rank = min(7 - (match_count + zero_count), 6)
    worst_rank = min(7 - match_count, 6)

    return [best_rank, worst_rank]