class Solution {
    public String solution(String my_string, String letter) {
        char target = letter.charAt(0);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < my_string.length(); i++) {
            char ch = my_string.charAt(i);
            if (ch != target) {
                sb.append(ch);
            }
        }

        return sb.toString();
    }
}