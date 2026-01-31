import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[] solveOne(String s) {
        int l = 0, r = s.length() - 1;
        int cnt = 0;

        while (true) {
            cnt++;
            if (l >= r) return new int[]{1, cnt};
            if (s.charAt(l) != s.charAt(r)) return new int[]{0, cnt};
            l++;
            r--;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < T; i++) {
            String s = br.readLine().trim();
            int[] ans = solveOne(s);
            sb.append(ans[0]).append(' ').append(ans[1]).append('\n');
        }
        System.out.print(sb.toString());
    }
}