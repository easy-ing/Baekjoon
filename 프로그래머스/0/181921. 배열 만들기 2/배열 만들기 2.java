import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> res = new ArrayList<>();

        for (int x = l; x <= r; x++) {
            if (onlyZeroOrFive(x)) res.add(x);
        }

        if (res.isEmpty()) return new int[]{-1};

        int[] ans = new int[res.size()];
        for (int i = 0; i < res.size(); i++) ans[i] = res.get(i);
        return ans;
    }

    private boolean onlyZeroOrFive(int x) {
        while (x > 0) {
            int d = x % 10;
            if (d != 0 && d != 5) return false;
            x /= 10;
        }
        return true;
    }
}