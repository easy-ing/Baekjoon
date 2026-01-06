class Solution {
    public int solution(String number) {
        int mod = 0;
        for (int i = 0; i < number.length(); i++) {
            int digit = number.charAt(i) - '0';
            mod = (mod + digit) % 9;
        }
        return mod;
    }
}