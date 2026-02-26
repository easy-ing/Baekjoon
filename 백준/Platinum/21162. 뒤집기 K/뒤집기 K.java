import java.io.*;
import java.util.*;

public class Main {

    // Build suffix array for int array s (0-based), values should be >= 1.
    // Complexity: O(n log n) with counting sorts (radix in each doubling step).
    static int[] buildSuffixArray(int[] s) {
        int n = s.length;
        int[] sa = new int[n];
        int[] rank = new int[n];
        int[] tmp = new int[n];

        // Initial ranks (ensure >= 1). We'll also allow 0 as "out of range" in second key.
        int maxv = 0;
        for (int i = 0; i < n; i++) {
            sa[i] = i;
            rank[i] = s[i];
            if (rank[i] > maxv) maxv = rank[i];
        }

        for (int k = 1; k < n; k <<= 1) {
            // Radix sort by (rank[i], rank[i+k]) using counting sort:
            // 1) sort by second key
            countingSortByKey(sa, rank, k, n, maxv);
            // 2) sort by first key (k=0 means rank[i])
            countingSortByKey(sa, rank, 0, n, maxv);

            // Recompute tmp ranks
            tmp[sa[0]] = 1;
            int classes = 1;

            for (int i = 1; i < n; i++) {
                int a = sa[i - 1];
                int b = sa[i];

                int a1 = rank[a];
                int b1 = rank[b];

                int a2 = (a + k < n) ? rank[a + k] : 0;
                int b2 = (b + k < n) ? rank[b + k] : 0;

                if (a1 != b1 || a2 != b2) classes++;
                tmp[b] = classes;
            }

            // swap rank and tmp
            int[] swap = rank;
            rank = tmp;
            tmp = swap;

            maxv = classes;
            if (classes == n) break;
        }

        return sa;
    }

    // Stable counting sort of sa by key = (pos+offset < n ? rank[pos+offset] : 0)
    // rank values in [1..maxRank], key in [0..maxRank]
    static void countingSortByKey(int[] sa, int[] rank, int offset, int n, int maxRank) {
        int[] cnt = new int[maxRank + 1 + 1]; // include 0..maxRank
        int[] out = new int[n];

        for (int i = 0; i < n; i++) {
            int pos = sa[i];
            int key = (pos + offset < n) ? rank[pos + offset] : 0;
            cnt[key]++;
        }

        // prefix sums -> positions
        int sum = 0;
        for (int i = 0; i < cnt.length; i++) {
            int c = cnt[i];
            cnt[i] = sum;
            sum += c;
        }

        for (int i = 0; i < n; i++) {
            int pos = sa[i];
            int key = (pos + offset < n) ? rank[pos + offset] : 0;
            out[cnt[key]++] = pos;
        }

        System.arraycopy(out, 0, sa, 0, n);
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);

        int N = fs.nextInt();
        int K = fs.nextInt();

        int[] A = new int[N];
        for (int i = 0; i < N; i++) A[i] = fs.nextInt();

        // B = reverse(A)
        int[] B = new int[N];
        for (int i = 0; i < N; i++) B[i] = A[N - 1 - i];

        // BB = B + B
        int[] BB = new int[2 * N];
        for (int i = 0; i < N; i++) {
            BB[i] = B[i];
            BB[i + N] = B[i];
        }

        int[] sa = buildSuffixArray(BB);

        int count = 0;
        int start = -1;
        for (int idx = 0; idx < sa.length; idx++) {
            int p = sa[idx];
            // rotations: start positions 1..N-1 (exclude 0, and exclude >=N)
            if (1 <= p && p <= N - 1) {
                count++;
                if (count == K) {
                    start = p;
                    break;
                }
            }
        }

        // Output BB[start..start+N-1]
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            if (i > 0) sb.append(' ');
            sb.append(BB[start + i]);
        }
        System.out.println(sb.toString());
    }

    // Simple fast scanner
    static class FastScanner {
        private final InputStream in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;

        FastScanner(InputStream is) { in = is; }

        private int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }

        int nextInt() throws IOException {
            int c;
            do c = read(); while (c <= ' ');

            int val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val;
        }
    }
}