class Solution {
    public int[] solution(int[] num_list, int n) {
        int len = num_list.length;
        int size = (len + n - 1) / n;  // 0, n, 2n... 개수
        int[] answer = new int[size];

        int idx = 0;
        for (int i = 0; i < len; i += n) {
            answer[idx++] = num_list[i];
        }
        return answer;
    }
}