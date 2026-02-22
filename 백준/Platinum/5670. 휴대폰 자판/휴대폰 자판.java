import java.io.*;
import java.util.*;

public class Main {

    // 빠른 입력 (EOF 처리 가능)
    static class FastScanner {
        private final InputStream in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;

        FastScanner(InputStream in) { this.in = in; }

        private int readByte() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }

        String next() throws IOException {
            StringBuilder sb = new StringBuilder();
            int c;
            do {
                c = readByte();
                if (c == -1) return null; // EOF
            } while (c <= ' ');

            while (c > ' ') {
                sb.append((char) c);
                c = readByte();
            }
            return sb.toString();
        }

        Integer nextInt() throws IOException {
            String s = next();
            if (s == null) return null;
            return Integer.parseInt(s);
        }
    }

    // 배열 기반 Trie (노드 총합: 단어 길이 합 + 1)
    static class Trie {
        int[][] next;       // next[node][ch] = child node index (0이면 없음)
        int[] childCount;   // 해당 노드의 자식 개수
        boolean[] isEnd;    // 단어 끝 여부
        int nodes;          // 사용 중인 노드 수 (0 = root)

        Trie(int maxNodes) {
            next = new int[maxNodes][26];
            childCount = new int[maxNodes];
            isEnd = new boolean[maxNodes];
            nodes = 1; // root = 0, 다음 할당은 1부터
        }

        void insert(String s) {
            int cur = 0;
            for (int i = 0; i < s.length(); i++) {
                int c = s.charAt(i) - 'a';
                int nx = next[cur][c];
                if (nx == 0) {
                    nx = nodes++;
                    next[cur][c] = nx;
                    childCount[cur]++; // cur의 자식 하나 늘어남
                }
                cur = nx;
            }
            isEnd[cur] = true;
        }

        int countKeystrokes(String s) {
            // 첫 글자는 무조건 입력
            int strokes = 1;
            int cur = 0;

            // 첫 글자로 이동
            int first = s.charAt(0) - 'a';
            cur = next[cur][first];

            // 2번째 글자부터 조건 체크
            for (int i = 1; i < s.length(); i++) {
                // "현재 노드(cur)" 기준으로 다음 글자를 눌러야 하는지 결정
                if (childCount[cur] > 1 || isEnd[cur]) strokes++;

                int c = s.charAt(i) - 'a';
                cur = next[cur][c];
            }
            return strokes;
        }
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);
        StringBuilder out = new StringBuilder();

        while (true) {
            Integer nObj = fs.nextInt();
            if (nObj == null) break; // EOF
            int N = nObj;

            String[] words = new String[N];
            int totalLen = 0;
            for (int i = 0; i < N; i++) {
                words[i] = fs.next();
                totalLen += words[i].length();
            }

            Trie trie = new Trie(totalLen + 1);
            for (String w : words) trie.insert(w);

            long sum = 0;
            for (String w : words) sum += trie.countKeystrokes(w);

            double avg = (double) sum / N;
            out.append(String.format(Locale.US, "%.2f", avg)).append('\n');
        }

        System.out.print(out);
    }
}