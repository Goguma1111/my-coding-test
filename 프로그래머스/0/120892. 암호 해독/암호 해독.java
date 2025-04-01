    class Solution { // 암호 해독
        public static String solution(String cipher, int code) {
            String answer = "";

            for(int i = 1; i <= cipher.length() / code; i++){
                answer += cipher.charAt((code * i) -1 );
            }
            return answer;
        }

        public static void main(String[] args) {
            System.out.println(solution("pfqallllabwaoclk", 2));
        }
    }
