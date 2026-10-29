def solution(m, n, puddles):
    MOD = 1_000_000_007

    # dp[y][x]: (x, y)까지 도달하는 최단경로의 수
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 집에서 출발
    dp[1][1] = 1

    # 웅덩이 좌표를 빠르게 확인할 수 있도록 집합으로 변환
    puddles = set(map(tuple, puddles))

    for y in range(1, n + 1):
        for x in range(1, m + 1):
            # 집은 이미 1로 초기화되어 있으므로 건너뜀
            if x == 1 and y == 1:
                continue

            # 웅덩이는 지나갈 수 없음
            if (x, y) in puddles:
                dp[y][x] = 0
                continue

            # 위쪽과 왼쪽에서 오는 경로 수를 합산
            dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % MOD

    return dp[n][m]