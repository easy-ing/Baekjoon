def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(fatigue, count):
        nonlocal answer

        # 현재까지 탐험한 던전 수의 최댓값 갱신
        answer = max(answer, count)

        for i in range(len(dungeons)):
            required, consume = dungeons[i]

            # 이미 탐험한 던전은 건너뜀
            if visited[i]:
                continue

            # 현재 피로도로 탐험할 수 없는 던전
            if fatigue < required:
                continue

            # 던전 탐험
            visited[i] = True
            dfs(fatigue - consume, count + 1)
            visited[i] = False

    dfs(k, 0)

    return answer