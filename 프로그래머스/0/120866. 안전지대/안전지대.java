class Solution {
    public int solution(int[][] board) {
        int n = board.length;

        // 위험지역 표시용 배열 (true = 위험)
        boolean[][] danger = new boolean[n][n];

        // 8방향(자기 자신 포함) 이동 벡터
        int[] dx = {-1, -1, -1, 0, 0, 0, 1, 1, 1};
        int[] dy = {-1,  0,  1,-1, 0, 1,-1, 0, 1};

        // 1) 지뢰(1)를 찾으면 주변 8칸 + 자기 자신을 위험지역으로 체크
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 1) {
                    for (int k = 0; k < 9; k++) {
                        int ni = i + dx[k];
                        int nj = j + dy[k];

                        // 범위 밖이면 스킵
                        if (ni < 0 || ni >= n || nj < 0 || nj >= n) continue;

                        danger[ni][nj] = true;
                    }
                }
            }
        }

        // 2) danger가 false인 칸(위험 표시 안 된 칸) = 안전지역 카운트
        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!danger[i][j]) answer++;
            }
        }

        return answer;
    }
}