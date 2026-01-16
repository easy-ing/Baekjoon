class Solution {
    public int[] solution(int[][] score) {
        int n = score.length;
        int[] answer = new int[n];

        // 평균 대신 합(eng + math)으로 비교하면 실수 처리 필요 없음 (2로 나누는 건 동일)
        int[] sum = new int[n];
        for (int i = 0; i < n; i++) {
            sum[i] = score[i][0] + score[i][1];
        }

        for (int i = 0; i < n; i++) {
            int rank = 1;
            for (int j = 0; j < n; j++) {
                if (sum[j] > sum[i]) rank++; // 나보다 평균(합)이 큰 사람이 있으면 등수 밀림
            }
            answer[i] = rank;
        }

        return answer;
    }
}