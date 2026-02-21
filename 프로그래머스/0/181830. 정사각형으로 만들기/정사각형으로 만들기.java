import java.util.*;

class Solution {
    public int[][] solution(int[][] arr) {
        int n = arr.length;        // 행 개수
        int m = arr[0].length;     // 열 개수
        int size = Math.max(n, m);

        int[][] answer = new int[size][size]; // 기본값 0
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                answer[i][j] = arr[i][j];
            }
        }
        return answer;
    }
}