import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> arr_list = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            // 마지막 원소 무조건 추가
            if (i == arr.length - 1) {
                arr_list.add(arr[i]);
            }
         
            else if (arr[i] != arr[i + 1]) {
                arr_list.add(arr[i]);
            }
        }

        int[] answer = new int[arr_list.size()];
        for (int i = 0; i < arr_list.size(); i++) {
            answer[i] = arr_list.get(i);
        }

        return answer;
    }
}