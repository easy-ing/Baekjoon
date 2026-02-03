class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        int a = -1, b = -1, c = -1;          // 학생 번호
        int ra = 101, rb = 101, rc = 101;    // 해당 학생의 등수 (최대 100이므로 101로 초기화)

        for (int i = 0; i < rank.length; i++) {
            if (!attendance[i]) continue;

            int r = rank[i];

            // 1등 후보 갱신
            if (r < ra) {
                rc = rb; c = b;
                rb = ra; b = a;
                ra = r;  a = i;
            }
            // 2등 후보 갱신
            else if (r < rb) {
                rc = rb; c = b;
                rb = r;  b = i;
            }
            // 3등 후보 갱신
            else if (r < rc) {
                rc = r;  c = i;
            }
        }

        return 10000 * a + 100 * b + c;
    }
}