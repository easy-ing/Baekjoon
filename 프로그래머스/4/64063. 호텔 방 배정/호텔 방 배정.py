def solution(k, room_number):
    parent = {}
    answer = []

    def find(x):
        visited = []

        while x in parent:
            visited.append(x)
            x = parent[x]

        empty_room = x
        parent[empty_room] = empty_room + 1

        for v in visited:
            parent[v] = empty_room + 1

        return empty_room

    for room in room_number:
        answer.append(find(room))

    return answer