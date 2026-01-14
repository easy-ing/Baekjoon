import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);

        int n = fs.nextInt();
        int m = fs.nextInt();

        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = fs.nextInt();

        Arrays.sort(a);

        int best = 0;

        for (int i = 0; i < n - 2; i++) {
            int l = i + 1;
            int r = n - 1;

            while (l < r) {
                int sum = a[i] + a[l] + a[r];

                if (sum == m) {
                    System.out.println(m);
                    return;
                }

                if (sum < m) {
                    if (sum > best) best = sum;
                    l++; // 더 큰 합을 노림
                } else {
                    r--; // 합이 너무 크니 줄임
                }
            }
        }

        System.out.println(best);
    }

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
            do { c = readByte(); } while (c <= ' ');

            int sign = 1;
            if (c == '-') { sign = -1; c = readByte(); }

            int val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = readByte();
            }
            return val * sign;
        }
    }
}