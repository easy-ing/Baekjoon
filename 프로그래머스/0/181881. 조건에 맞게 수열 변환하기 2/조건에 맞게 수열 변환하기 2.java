class Solution {
    public int solution(int[] arr) {
        int answer = 0;

        for (int v : arr) {
            int cnt = 0;
            int x = v;

            while (true) {
                int next = x;

                if (x >= 50 && x % 2 == 0) {
                    next = x / 2;
                } else if (x < 50 && x % 2 == 1) {
                    next = x * 2 + 1;
                }

                if (next == x) break; 
                x = next;
                cnt++;
            }

            if (cnt > answer) answer = cnt; 
        }

        return answer;
    }
}