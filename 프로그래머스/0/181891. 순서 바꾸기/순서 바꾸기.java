class Solution {
    public int[] solution(int[] num_list, int n) {
        int len = num_list.length;
        int[] answer = new int[len];

        int idx = 0;

        // n번째 이후 원소들: 인덱스 n ~ len-1
        for (int i = n; i < len; i++) {
            answer[idx++] = num_list[i];
        }

        // n번째까지 원소들: 인덱스 0 ~ n-1
        for (int i = 0; i < n; i++) {
            answer[idx++] = num_list[i];
        }

        return answer;
    }
}