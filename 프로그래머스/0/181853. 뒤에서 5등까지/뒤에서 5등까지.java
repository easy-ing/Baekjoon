import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        Arrays.sort(num_list);                 // 오름차순 정렬
        return Arrays.copyOf(num_list, 5);     // 앞 5개 반환
    }
}