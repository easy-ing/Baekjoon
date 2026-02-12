import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        long M = Long.parseLong(st.nextToken());

        long[] trees = new long[N];
        st = new StringTokenizer(br.readLine());

        long max = 0;
        for (int i = 0; i < N; i++) {
            trees[i] = Long.parseLong(st.nextToken());
            if (trees[i] > max) max = trees[i];
        }

        long left = 0;
        long right = max;
        long answer = 0;

        while (left <= right) {
            long mid = (left + right) / 2; // 절단기 높이 후보

            long wood = 0;
            for (long h : trees) {
                if (h > mid) wood += (h - mid);
            }

            if (wood >= M) {      // M 이상 확보 가능 -> 높이를 더 올려본다(최댓값 찾기)
                answer = mid;
                left = mid + 1;
            } else {              // 부족 -> 높이를 낮춘다
                right = mid - 1;
            }
        }

        System.out.println(answer);
    }
}