import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        int[] stack = new int[N]; // 최대 N번 push 가능
        int top = 0;              // 현재 스택 크기(= 다음에 들어갈 위치)

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            int cmd = line.charAt(0) - '0';

            if (cmd == 1) {
                // "1 X"
                int x = Integer.parseInt(line.substring(2));
                stack[top++] = x;
            } else if (cmd == 2) {
                if (top == 0) sb.append("-1\n");
                else sb.append(stack[--top]).append('\n');
            } else if (cmd == 3) {
                sb.append(top).append('\n');
            } else if (cmd == 4) {
                sb.append(top == 0 ? 1 : 0).append('\n');
            } else { // cmd == 5
                if (top == 0) sb.append("-1\n");
                else sb.append(stack[top - 1]).append('\n');
            }
        }

        System.out.print(sb.toString());
    }
}