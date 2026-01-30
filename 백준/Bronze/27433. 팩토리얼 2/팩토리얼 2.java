import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        long fact = 1L;
        for (int i = 2; i <= n; i++) {
            fact *= i;
        }

        System.out.println(fact);
    }
}