import java.util.*;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        List<Integer> x = new ArrayList<>();
        
        for (int i = 0; i < arr.length; i++) {
            int a = arr[i];
            
            if (flag[i]) {
                // arr[i]를 arr[i] * 2번 추가
                for (int k = 0; k < a * 2; k++) {
                    x.add(a);
                }
            } else {
                // 마지막 arr[i]개 원소 제거
                for (int k = 0; k < a; k++) {
                    x.remove(x.size() - 1);
                }
            }
        }
        
        int[] answer = new int[x.size()];
        for (int i = 0; i < x.size(); i++) {
            answer[i] = x.get(i);
        }
        return answer;
    }
}