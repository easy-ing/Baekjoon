class Solution {
    public int solution(String[] order) {
        int total = 0;

        for (String o : order) {
            if (o.equals("anything")) {
                total += 4500;
            } else if (o.contains("americano")) {
                total += 4500;
            } else if (o.contains("cafelatte")) {
                total += 5000;
            }
        }

        return total;
    }
}