import java.util.Arrays;

class Solution {
    public int solution(String[] spell, String[] dic) {
        // 1) spell을 정렬해서 기준 키 만들기
        Arrays.sort(spell);
        String target = String.join("", spell);

        // 2) dic의 각 단어를 정렬한 결과가 target과 같은지 검사
        for (String word : dic) {
            if (word.length() != target.length()) continue; // 길이 다르면 절대 불가능

            char[] arr = word.toCharArray();
            Arrays.sort(arr);
            String sortedWord = new String(arr);

            if (sortedWord.equals(target)) return 1;
        }

        return 2;
    }
}