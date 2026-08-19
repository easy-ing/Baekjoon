import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while scoville:
        if scoville[0] >= K:
            return answer

        if len(scoville) < 2:
            return -1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new = first + second * 2
        heapq.heappush(scoville, new)

        answer += 1

    return -1