def solution(s):
    s = s[2:-2]
    groups = s.split("},{")

    groups = [list(map(int, group.split(","))) for group in groups]
    groups.sort(key=len)

    answer = []
    visited = set()

    for group in groups:
        for num in group:
            if num not in visited:
                visited.add(num)
                answer.append(num)

    return answer