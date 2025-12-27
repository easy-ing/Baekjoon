class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        for (int q = 0; q < queries.length; q++) {
            int i = queries[q][0];
            int j = queries[q][1];

            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        return arr;
    }
}