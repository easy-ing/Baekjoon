class Solution {
    public int solution(int[] numbers, int k) {
        int len = numbers.length;
        int idx = (2 * (k - 1)) % len;
        return numbers[idx];
    }
}