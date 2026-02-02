class Solution {
    public int[] solution(int[] arr, int n) {
        int start = (arr.length % 2 == 1) ? 0 : 1; // 홀수 길이 -> 0부터, 짝수 길이 -> 1부터

        for (int i = start; i < arr.length; i += 2) {
            arr[i] += n;
        }

        return arr;
    }
}