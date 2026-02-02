import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        int n = arr.length;

        int size = 1;
        while (size < n) {
            size *= 2;
        }

        if (size == n) return arr;

        int[] answer = new int[size];
        System.arraycopy(arr, 0, answer, 0, n); // 뒤는 자동으로 0 채워짐
        return answer;
    }
}