class Solution {
    public String[] solution(String[] picture, int k) {
        int h = picture.length;            // 원본 세로 길이
        String[] answer = new String[h * k]; // 확대 후 세로 길이 = h * k
        int idx = 0;

        for (String row : picture) {
            // 1) 가로 k배 확장한 한 줄 만들기
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < row.length(); i++) {
                char ch = row.charAt(i);
                for (int t = 0; t < k; t++) sb.append(ch);
            }
            String expandedRow = sb.toString();

            // 2) 세로 k배: 같은 줄을 k번 추가
            for (int t = 0; t < k; t++) {
                answer[idx++] = expandedRow;
            }
        }

        return answer;
    }
}