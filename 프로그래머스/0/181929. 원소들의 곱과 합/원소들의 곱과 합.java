class Solution {
    public int solution(int[] num_list) {
        int sum = 0;
        int prod = 1;

        for (int x : num_list) {
            sum += x;
            prod *= x;
        }

        return (prod < sum * sum) ? 1 : 0;
    }
}