from collections import deque

def solution(n, wires):
    answer = n

    for cut in range(len(wires)):
        graph = [[] for _ in range(n + 1)]

        # cut번째 전선만 빼고 그래프 만들기
        for i, (a, b) in enumerate(wires):
            if i == cut:
                continue
            graph[a].append(b)
            graph[b].append(a)

        # 1번 송전탑 쪽 네트워크 개수 세기
        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True
        count = 1

        while queue:
            now = queue.popleft()

            for next_node in graph[now]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    count += 1

        other = n - count
        answer = min(answer, abs(count - other))

    return answer