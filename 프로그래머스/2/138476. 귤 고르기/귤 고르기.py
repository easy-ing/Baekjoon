from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)

    answer = 0
    for count in sorted(counter.values(), reverse=True):
        k -= count
        answer += 1
        if k <= 0:
            break

    return answer