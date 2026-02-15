import java.io.*;
import java.util.*;

public class Main {

    // 매우 빠른 입력 (N=1,000,000 대응)
    static class FastScanner {
        private final InputStream in = System.in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;

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
            } while (c <= ' '); // skip spaces

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

    // tails[0..size-1]에서 x 이상이 처음 나오는 위치
    static int lowerBound(int[] tails, int size, int x) {
        int l = 0, r = size; // [l, r)
        while (l < r) {
            int m = (l + r) >>> 1;
            if (tails[m] >= x) r = m;
            else l = m + 1;
        }
        return l;
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int[] tails = new int[N]; // 최대 길이 N
        int size = 0;

        for (int i = 0; i < N; i++) {
            int a = fs.nextInt();

            if (size == 0 || tails[size - 1] < a) {
                tails[size++] = a;
            } else {
                int pos = lowerBound(tails, size, a);
                tails[pos] = a;
            }
        }

        System.out.println(size);
    }
}