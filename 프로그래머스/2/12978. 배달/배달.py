import heapq


def solution(N, road, K):
    # 인접 리스트
    graph = [[] for _ in range(N + 1)]

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 1번 마을에서 각 마을까지의 최단 거리
    dist = [float('inf')] * (N + 1)
    dist[1] = 0

    # (거리, 마을 번호)
    heap = [(0, 1)]

    while heap:
        current_dist, current = heapq.heappop(heap)

        # 이미 더 짧은 거리로 처리된 경우
        if current_dist > dist[current]:
            continue

        for next_node, weight in graph[current]:
            new_dist = current_dist + weight

            # 더 짧은 경로를 발견한 경우
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    # K 이하로 배달 가능한 마을의 수
    return sum(distance <= K for distance in dist[1:])