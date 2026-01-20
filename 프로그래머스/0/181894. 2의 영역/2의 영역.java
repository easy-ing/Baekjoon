class Solution {
    public int[] solution(int[] arr) {
        int first = -1;
        int last = -1;

        // 첫 번째 2 찾기
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                first = i;
                break;
            }
        }

        // 2가 없으면 [-1]
        if (first == -1) return new int[]{-1};

        // 마지막 2 찾기
        for (int i = arr.length - 1; i >= 0; i--) {
            if (arr[i] == 2) {
                last = i;
                break;
            }
        }

        // first ~ last (닫힌 구간) 복사
        int[] answer = new int[last - first + 1];
        for (int i = first; i <= last; i++) {
            answer[i - first] = arr[i];
        }

        return answer;
    }
}