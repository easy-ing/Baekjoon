import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long left = 1L;
        int max = 0;
        for (int t : times) {
            if (t > max) max = t;
        }
        long right = (long) max * (long) n;
        long answer = right;

        while (left <= right) {
            long mid = (left + right) / 2; 
            long processed = 0L;
            for (int t : times) {
                processed += mid / t;
                if (processed >= n) break; 
            }
            if (processed >= n) {  
                answer = mid;     
                right = mid - 1;   
            } else {               
                left = mid + 1;
            }
        }
        return answer;
    }
}