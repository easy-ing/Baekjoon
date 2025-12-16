import java.util.Arrays;

class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int len = numbers.length;
        double count = 0;
        for(int i=0;i<len;i++){
            count += numbers[i];
        }
        answer = count / len;
        return answer;
    }
}