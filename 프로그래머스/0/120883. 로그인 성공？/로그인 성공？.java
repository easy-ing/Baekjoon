class Solution {
    public String solution(String[] id_pw, String[][] db) {
        String id = id_pw[0];
        String pw = id_pw[1];

        for (int i = 0; i < db.length; i++) {
            String dbId = db[i][0];
            String dbPw = db[i][1];

            if (dbId.equals(id)) {          
                if (dbPw.equals(pw)) {      
                    return "login";
                } else {                    
                    return "wrong pw";
                }
            }
        }

        return "fail";
    }
}