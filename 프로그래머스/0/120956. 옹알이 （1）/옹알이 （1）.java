class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] sounds = {"aya", "ye", "woo", "ma"};

        for (String word : babbling) {
            int idx = 0;

            while (idx < word.length()) {
                boolean matched = false;

                for (String s : sounds) {
                    if (word.startsWith(s, idx)) {
                        idx += s.length();
                        matched = true;
                        break;
                    }
                }

                if (!matched) break; // 여기서부터는 어떤 발음도 못 붙임 -> 실패
            }

            if (idx == word.length()) answer++; // 끝까지 정확히 잘라냈으면 성공
        }

        return answer;
    }
}