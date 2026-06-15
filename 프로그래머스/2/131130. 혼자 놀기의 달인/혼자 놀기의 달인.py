def solution(cards):
    visited = [False] * len(cards)
    groups = []

    for i in range(len(cards)):
        if not visited[i]:
            count = 0
            current = i

            while not visited[current]:
                visited[current] = True
                count += 1
                current = cards[current] - 1

            groups.append(count)

    groups.sort(reverse=True)

    if len(groups) < 2:
        return 0

    return groups[0] * groups[1]