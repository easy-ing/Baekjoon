class Solution {
    public int solution(int a, int b) {
        int limit = Math.min(a, b);

        for (int i = 2; i <= limit; i++) {
            while (a % i == 0 && b % i == 0) {
                a /= i;
                b /= i;
                limit = Math.min(a, b);
            }
        }

        while (b % 2 == 0) b /= 2;
        while (b % 5 == 0) b /= 5;

        return b == 1 ? 1 : 2;
    }
}