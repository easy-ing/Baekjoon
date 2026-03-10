import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] A = new int[N];
        int[] B = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        int M = Integer.parseInt(br.readLine());

        int[] C = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            C[i] = Integer.parseInt(st.nextToken());
        }

        Deque<Integer> deque = new ArrayDeque<>();

        // 큐(0)인 자료구조의 초기값만 저장
        // 앞에서부터 확인하면서 addFirst 하면
        // 실제 출력 순서에 맞게 정리된다.
        for (int i = 0; i < N; i++) {
            if (A[i] == 0) {
                deque.addFirst(B[i]);
            }
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < M; i++) {
            deque.addLast(C[i]);
            sb.append(deque.pollFirst()).append(' ');
        }

        System.out.println(sb);
    }
}