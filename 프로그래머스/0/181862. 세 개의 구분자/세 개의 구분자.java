import java.util.*;

class Solution {
    public String[] solution(String myStr) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < myStr.length(); i++) {
            char ch = myStr.charAt(i);

            if (ch == 'a' || ch == 'b' || ch == 'c') {
                if (sb.length() > 0) {
                    result.add(sb.toString());
                    sb.setLength(0);
                }
            } else {
                sb.append(ch);
            }
        }

        // 마지막 토큰 처리
        if (sb.length() > 0) result.add(sb.toString());

        if (result.isEmpty()) return new String[] { "EMPTY" };
        return result.toArray(new String[0]);
    }
}