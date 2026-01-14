class Solution {
    public int solution(int[] sides) {
        int x = Math.min(sides[0], sides[1]); 
        return 2 * x - 1;
    }
}