import java.util.Arrays;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        Arrays.sort(rocks);
        
        int left = 1;
        int right = distance;
        
        // 바위의 거리의 최솟값을 기준으로 이분탐색
        while(left <= right) {
            int mid = (left + right) / 2;
            int deleteRocks = 0;
            int prevRock = 0;
            
            for(int rock: rocks) {
                if (Math.abs(rock - prevRock) < mid) {
                    deleteRocks++;
                } else {
                    prevRock = rock;
                }
            }
            
            if (distance - prevRock < mid) {
                deleteRocks++;
            }
            
            if (deleteRocks > n) {
                right = mid - 1;
            } else if (deleteRocks <= n) {
                left = mid + 1;
                answer = mid;
            }
        }
        
        return answer;
    }
}