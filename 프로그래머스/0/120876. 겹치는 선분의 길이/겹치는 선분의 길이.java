import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(int[][] lines) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int i=0; i<lines.length; i++) {
            for(int j=lines[i][0]; j<lines[i][1]; j++) {
                map.put(j, map.getOrDefault(j, 0)+1);
            }
        }
        
        int answer = 0;
        for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if(entry.getValue() > 1) {
                answer++;
            }
        }
        return answer;
    }
}