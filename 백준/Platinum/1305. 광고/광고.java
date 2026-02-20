import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int L = Integer.parseInt(br.readLine().trim());
        String S = br.readLine().trim();

        int[] pi = new int[L];
        int j = 0;

        for (int i = 1; i < L; i++) {
            while (j > 0 && S.charAt(i) != S.charAt(j)) {
                j = pi[j - 1];
            }
            if (S.charAt(i) == S.charAt(j)) {
                pi[i] = ++j;
            }
        }

        System.out.println(L - pi[L - 1]);
    }
}