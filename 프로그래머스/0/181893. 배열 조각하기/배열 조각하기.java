class Solution {
    public int[] solution(int[] arr, int[] query) {
        int left = 0;
        int right = arr.length - 1;

        for (int i = 0; i < query.length; i++) {
            int q = query[i];

            if (i % 2 == 0) {
                // 짝수 인덱스: q 뒤를 자름 -> [left .. left+q]만 남김
                right = left + q;
            } else {
                // 홀수 인덱스: q 앞을 자름(단 q는 남김) -> [left+q .. right]만 남김
                left = left + q;
            }
        }

        int[] answer = new int[right - left + 1];
        for (int i = left; i <= right; i++) {
            answer[i - left] = arr[i];
        }

        return answer;
    }
}