import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Long.parseLong(br.readLine().trim());

        long ans = (long) Math.sqrt(N); // floor(sqrt(N))
        System.out.println(ans);
    }
}