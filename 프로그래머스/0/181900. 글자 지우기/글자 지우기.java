class Solution {
    public String solution(String my_string, int[] indices) {
        int n = my_string.length();
        boolean[] remove = new boolean[n];

        for (int idx : indices) {
            remove[idx] = true;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (!remove[i]) sb.append(my_string.charAt(i));
        }

        return sb.toString();
    }
}