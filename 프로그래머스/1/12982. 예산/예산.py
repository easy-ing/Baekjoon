def solution(d, budget):
    answer = 0

    for cost in sorted(d):
        if budget < cost:
            break
        budget -= cost
        answer += 1

    return answer