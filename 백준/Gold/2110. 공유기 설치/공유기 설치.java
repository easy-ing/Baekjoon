import java.io.*;
import java.util.*;

public class Main {
    static int N, C;
    static int[] x;

    // 거리 d 이상으로 공유기 C개 설치 가능?
    static boolean canInstall(int d) {
        int count = 1;          // 첫 집에는 무조건 설치
        int last = x[0];

        for (int i = 1; i < N; i++) {
            if (x[i] - last >= d) {
                count++;
                last = x[i];
                if (count >= C) return true; // C개 설치 완료
            }
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        x = new int[N];
        for (int i = 0; i < N; i++) x[i] = Integer.parseInt(br.readLine());

        Arrays.sort(x);

        int lo = 1;                 // 최소 거리 (집 좌표가 겹치지 않으므로 1부터 시작 가능)
        int hi = x[N - 1] - x[0];    // 최대 거리 (양 끝집)
        int ans = 0;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;

            if (canInstall(mid)) {
                ans = mid;      // mid 가능 -> 일단 답 후보
                lo = mid + 1;   // 더 큰 거리 시도
            } else {
                hi = mid - 1;   // mid 불가능 -> 거리 줄이기
            }
        }

        System.out.println(ans);
    }
}