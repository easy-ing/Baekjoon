import java.io.*;
import java.util.*;

public class Main {

    static class Node {
        Node[] next = new Node[2];
    }

    static class BitTrie {
        Node root = new Node();

        void insert(int x) {
            Node cur = root;
            for (int b = 30; b >= 0; b--) {
                int bit = (x >>> b) & 1;
                if (cur.next[bit] == null) cur.next[bit] = new Node();
                cur = cur.next[bit];
            }
        }

        int maxXor(int x) {
            Node cur = root;
            int res = 0;
            for (int b = 30; b >= 0; b--) {
                int bit = (x >>> b) & 1;
                int want = bit ^ 1; // 반대 비트면 XOR가 1
                if (cur.next[want] != null) {
                    res |= (1 << b);
                    cur = cur.next[want];
                } else {
                    cur = cur.next[bit];
                }
            }
            return res;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) arr[i] = Integer.parseInt(st.nextToken());

        BitTrie trie = new BitTrie();
        trie.insert(arr[0]);

        int ans = 0;
        for (int i = 1; i < N; i++) {
            ans = Math.max(ans, trie.maxXor(arr[i]));
            trie.insert(arr[i]);
        }

        System.out.println(ans);
    }
}