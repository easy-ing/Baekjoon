class Solution {
    public String solution(String myString) {
        StringBuilder sb = new StringBuilder(myString.length());

        for (int i = 0; i < myString.length(); i++) {
            char ch = myString.charAt(i);
            // 'l'보다 앞(작은) 문자면 'l'로 교체
            if (ch < 'l') sb.append('l');
            else sb.append(ch);
        }

        return sb.toString();
    }
}