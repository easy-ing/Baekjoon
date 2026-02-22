class Solution {
    public int solution(int[][] board, int k) {
        int n = board.length;
        int m = board[0].length;
        int sum = 0;

        for (int i = 0; i < n; i++) {
            int maxJ = k - i;
            if (maxJ < 0) break;              
            if (maxJ >= m) maxJ = m - 1;      // 열 범위를 넘으면 끝열로 clamp

            for (int j = 0; j <= maxJ; j++) {
                sum += board[i][j];
            }
        }
        return sum;
    }
}