import java.io.*;
import java.util.*;

public class Main {

    // pi[i] = P[0..i]의 접두사이면서 접미사인 "최대 길이"
    static int[] buildPi(String p) {
        int m = p.length();
        int[] pi = new int[m];
        int j = 0; // 현재까지 일치한 접두사 길이

        for (int i = 1; i < m; i++) {
            while (j > 0 && p.charAt(i) != p.charAt(j)) {
                j = pi[j - 1];
            }
            if (p.charAt(i) == p.charAt(j)) {
                j++;
                pi[i] = j;
            }
        }
        return pi;
    }

    static List<Integer> kmpSearch(String t, String p) {
        int n = t.length();
        int m = p.length();
        int[] pi = buildPi(p);

        List<Integer> positions = new ArrayList<>();
        int j = 0; // 패턴에서 현재 비교 중인 위치(일치 길이)

        for (int i = 0; i < n; i++) {
            while (j > 0 && t.charAt(i) != p.charAt(j)) {
                j = pi[j - 1];
            }
            if (t.charAt(i) == p.charAt(j)) {
                j++;
                if (j == m) {
                    // 매칭 성공: 시작 위치는 (i - m + 1) (0-index), 출력은 1-index
                    positions.add((i - m + 1) + 1);
                    // 다음 매칭을 위해 점프
                    j = pi[j - 1];
                }
            }
        }
        return positions;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String T = br.readLine();
        String P = br.readLine();

        List<Integer> ans = kmpSearch(T, P);

        StringBuilder sb = new StringBuilder();
        sb.append(ans.size()).append('\n');
        for (int i = 0; i < ans.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(ans.get(i));
        }
        sb.append('\n');

        System.out.print(sb);
    }
}