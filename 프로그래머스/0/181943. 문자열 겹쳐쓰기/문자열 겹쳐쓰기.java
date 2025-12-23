class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        StringBuilder sb = new StringBuilder();

        String[] origin = my_string.split("");
        String[] over = overwrite_string.split("");

        for (int i = 0; i < s; i++) {
            sb.append(origin[i]);
        }

        for (int j = 0; j < over.length; j++) {
            sb.append(over[j]);
        }

        for (int k = s + over.length; k < origin.length; k++) {
            sb.append(origin[k]);
        }

        return sb.toString();
    }
}