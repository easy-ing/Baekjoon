class Solution {
    public int[][] solution(int n) {
        int[][] a = new int[n][n];

        // 시작 좌표
        int r = 0, c = 0;
        // 방향: 오른쪽, 아래, 왼쪽, 위
        int[] dr = {0, 1, 0, -1};
        int[] dc = {1, 0, -1, 0};
        int dir = 0;

        for (int num = 1; num <= n * n; num++) {
            a[r][c] = num;

            // 다음 칸 미리 계산
            int nr = r + dr[dir];
            int nc = c + dc[dir];

            // 범위를 벗어나거나 이미 채워진 칸이면 방향 전환
            if (nr < 0 || nr >= n || nc < 0 || nc >= n || a[nr][nc] != 0) {
                dir = (dir + 1) % 4;
                nr = r + dr[dir];
                nc = c + dc[dir];
            }

            r = nr;
            c = nc;
        }

        return a;
    }
}