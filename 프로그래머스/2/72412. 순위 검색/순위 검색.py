from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    applicants = defaultdict(list)
    answer = []

    for person in info:
        data = person.split()
        score = int(data[-1])
        conditions = data[:-1]

        for count in range(5):
            for combo in combinations(range(4), count):
                key = conditions[:]
                for i in combo:
                    key[i] = '-'
                applicants[tuple(key)].append(score)

    for scores in applicants.values():
        scores.sort()

    for q in query:
        data = q.replace(' and ', ' ').split()
        conditions = tuple(data[:4])
        score = int(data[4])

        scores = applicants[conditions]
        idx = bisect_left(scores, score)
        answer.append(len(scores) - idx)

    return answer