import java.io.*;
import java.util.*;

public class Main {

    // 빠른 입력
    static class FastScanner {
        private final InputStream in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;

        FastScanner(InputStream in) {
            this.in = in;
        }

        private int readByte() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }

        int nextInt() throws IOException {
            int c;
            do {
                c = readByte();
            } while (c <= ' ');

            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = readByte();
            }

            int val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = readByte();
            }
            return val * sign;
        }
    }

    static boolean[] sieve(int n) {
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        if (n >= 0) isPrime[0] = false;
        if (n >= 1) isPrime[1] = false;

        int limit = (int) Math.sqrt(n);
        for (int i = 2; i <= limit; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        return isPrime;
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);

        int T = fs.nextInt();
        int[] Ns = new int[T];
        int maxN = 0;
        for (int i = 0; i < T; i++) {
            Ns[i] = fs.nextInt();
            if (Ns[i] > maxN) maxN = Ns[i];
        }

        boolean[] isPrime = sieve(maxN);

        // 소수 리스트 (반복을 더 빠르게)
        int maxHalf = maxN / 2;
        int[] primes = new int[maxN]; // 충분히 크게
        int pc = 0;
        for (int i = 2; i <= maxHalf; i++) {
            if (isPrime[i]) primes[pc++] = i;
        }

        StringBuilder sb = new StringBuilder();
        for (int n : Ns) {
            int half = n / 2;
            int count = 0;
            for (int i = 0; i < pc; i++) {
                int p = primes[i];
                if (p > half) break;
                if (isPrime[n - p]) count++;
            }
            sb.append(count).append('\n');
        }

        System.out.print(sb.toString());
    }
}