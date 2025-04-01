class Solution { // 뒤집힌 문자열
    public static String solution(String my_string) {
        String answer = "";
        for (int i = my_string.length() -1 ; i >= 0; i--){
            answer += my_string.charAt(i);
        }
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution("jaron"));
    }
}