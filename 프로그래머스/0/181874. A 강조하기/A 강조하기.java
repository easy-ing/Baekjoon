class Solution {
    public String solution(String myString) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < myString.length(); i++) {
            char c = myString.charAt(i);

            if (c == 'a') {
                sb.append('A');
            } else if (c >= 'A' && c <= 'Z' && c != 'A') {
                sb.append((char)(c - 'A' + 'a')); // 소문자로
            } else {
                sb.append(c);
            }
        }

        return sb.toString();
    }
}