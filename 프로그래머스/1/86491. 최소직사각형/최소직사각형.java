class Solution {
    public int solution(int[][] sizes) {
        int walletW = 0;
        int walletH = 0;

        for (int[] s : sizes) {
            int w = s[0];
            int h = s[1];

            if (w < h) { // 더 긴 쪽을 가로로 두기
                int tmp = w;
                w = h;
                h = tmp;
            }

            walletW = Math.max(walletW, w);
            walletH = Math.max(walletH, h);
        }

        return walletW * walletH;
    }
}