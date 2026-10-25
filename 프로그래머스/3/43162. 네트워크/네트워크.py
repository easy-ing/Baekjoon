def solution(n, computers):
    visited = [False] * n
    answer = 0
    def dfs(computer):
        visited[computer] = True
        for next_computer in range(n):
            if computers[computer][next_computer] == 1 and not visited[next_computer]:
                dfs(next_computer)
    for computer in range(n):
        if not visited[computer]:
            dfs(computer)
            answer += 1
    return answer