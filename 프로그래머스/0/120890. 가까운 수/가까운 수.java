class Solution {
    public int solution(int[] array, int n) {
        int best = array[0];
        int bestDiff = Math.abs(best - n);

        for (int x : array) {
            int diff = Math.abs(x - n);
            if (diff < bestDiff || (diff == bestDiff && x < best)) {
                best = x;
                bestDiff = diff;
            }
        }
        return best;
    }
}