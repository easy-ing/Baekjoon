from collections import deque

def solution(n, roads, sources, destination):
    # 1. 인접 리스트 생성
    graph = [[] for _ in range(n + 1)]

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # 2. 거리 배열 초기화
    distance = [-1] * (n + 1)
    distance[destination] = 0

    # 3. BFS 시작
    queue = deque([destination])

    while queue:
        current = queue.popleft()

        for next_node in graph[current]:
            # 아직 방문하지 않은 지역만 탐색
            if distance[next_node] == -1:
                distance[next_node] = distance[current] + 1
                queue.append(next_node)

    # 4. 각 부대원의 최단거리 반환
    answer = [distance[source] for source in sources]

    return answer