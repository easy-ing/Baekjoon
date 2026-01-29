import java.util.*;

class Solution {
    public String[] solution(String myString) {
        String[] parts = myString.split("x");  // x 기준 분리
        ArrayList<String> list = new ArrayList<>();

        for (String p : parts) {
            if (!p.isEmpty()) list.add(p);     // 빈 문자열 제거
        }

        Collections.sort(list);                 // 사전순 정렬

        return list.toArray(new String[0]);
    }
}