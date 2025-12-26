import java.util.*;

class Solution {
    public int solution(int[] sides) {
        int[] temp = sides;
        Arrays.sort(temp);
        if(temp[0]+temp[1]>temp[2]){
            return 1;
        }else{
            return 2;
        }
    }
}