from collections import defaultdict

def solution(weights):
    answer = 0
    count = defaultdict(int)

    weights.sort()

    for w in weights:
        answer += count[w]

        if w * 2 % 3 == 0:
            answer += count[w * 2 // 3]

        if w % 2 == 0:
            answer += count[w // 2]

        if w * 3 % 4 == 0:
            answer += count[w * 3 // 4]

        count[w] += 1

    return answer