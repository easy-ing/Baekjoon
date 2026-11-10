def solution(n, costs):
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a == b:
            return False

        parent[b] = a
        return True

    # 건설 비용 기준 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    answer = 0
    count = 0

    for a, b, cost in costs:
        # 서로 다른 집합이라면 연결
        if union(a, b):
            answer += cost
            count += 1

        # 모든 섬이 연결되면 종료
        if count == n - 1:
            break

    return answer