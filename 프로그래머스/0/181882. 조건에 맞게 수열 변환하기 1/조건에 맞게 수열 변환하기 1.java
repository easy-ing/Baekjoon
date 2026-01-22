class Solution {
    public int[] solution(int[] arr) {
        int[] answer = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            int x = arr[i];

            if (x >= 50 && x % 2 == 0) {      // 50 이상 짝수
                x /= 2;
            } else if (x < 50 && x % 2 == 1) { // 50 미만 홀수
                x *= 2;
            }

            answer[i] = x;
        }

        return answer;
    }
}