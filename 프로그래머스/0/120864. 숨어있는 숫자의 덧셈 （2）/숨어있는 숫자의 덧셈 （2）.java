class Solution {
    public int solution(String my_string) {
        int answer = 0;
        int current = 0;

        for (int i = 0; i < my_string.length(); i++) {
            char ch = my_string.charAt(i);

            if (Character.isDigit(ch)) {
                current = current * 10 + (ch - '0');
            } else {
                answer += current;
                current = 0;
            }
        }
        answer += current;

        return answer;
    }
}