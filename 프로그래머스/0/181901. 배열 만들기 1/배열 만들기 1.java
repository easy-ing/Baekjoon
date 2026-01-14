class Solution {
    public int[] solution(int n, int k) {
        int size = n / k;          
        int[] answer = new int[size];

        for (int i = 1; i <= size; i++) {
            answer[i - 1] = k * i;
        }

        return answer;
    }
}