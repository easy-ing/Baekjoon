import heapq

def solution(n, k, enemy):
    heap = []

    for i, e in enumerate(enemy):
        heapq.heappush(heap, e)

        # 무적권을 초과한 적은 병사로 막는다.
        if len(heap) > k:
            n -= heapq.heappop(heap)

        # 병사가 부족하면 현재 라운드까지 진행할 수 없음
        if n < 0:
            return i

    return len(enemy)