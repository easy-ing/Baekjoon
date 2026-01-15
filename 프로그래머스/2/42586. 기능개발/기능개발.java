import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        int day = 0;

        for (int i = 0; i < progresses.length; i++) {
            int done = progresses[i] + speeds[i] * day;

            if (done < 100) {
                int remain = 100 - done;
                int need = (remain + speeds[i] - 1) / speeds[i];
                day += need;

                answer.add(1);
            } else {
                int last = answer.size() - 1;
                answer.set(last, answer.get(last) + 1);
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}