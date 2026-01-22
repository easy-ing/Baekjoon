class Solution {
    public int solution(int[] num_list) {
        int answer = 0;

        for (int x : num_list) {
            while (x > 1) {
                x /= 2;      // 짝수면 /2, 홀수면 (x-1)/2와 결과 동일
                answer++;    // 나누기 연산 1번 수행
            }
        }

        return answer;
    }
}