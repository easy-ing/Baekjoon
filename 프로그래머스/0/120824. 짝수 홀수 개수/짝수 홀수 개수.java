class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];
        int cnt_1 = 0; // 짝수 개수
        int cnt_2 = 0; // 홀수 개수

        for (int i = 0; i < num_list.length; i++) {
            if (num_list[i] % 2 == 0) {
                cnt_1++;
            } else {
                cnt_2++;
            }
        }

        answer[0] = cnt_1;
        answer[1] = cnt_2;

        return answer;
    }
}