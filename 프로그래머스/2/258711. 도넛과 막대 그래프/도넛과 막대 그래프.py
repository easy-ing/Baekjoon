def solution(edges):
    MAX = 1_000_001
    indeg = [0] * MAX
    outdeg = [0] * MAX
    for a, b in edges:
        outdeg[a] += 1
        indeg[b] += 1

    created = stick = eight = 0
    for v in range(1, MAX):
        if indeg[v] == 0 and outdeg[v] >= 2:
            created = v
        elif outdeg[v] == 0 and indeg[v] >= 1:
            stick += 1
        elif outdeg[v] == 2 and indeg[v] >= 2:
            eight += 1

    total = outdeg[created]
    donut = total - stick - eight
    return [created, donut, stick, eight]