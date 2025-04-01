class Solution { // 특정문자 제거하기
    public static String solution(String my_string, String letter) {
        String answer = "";
        answer = my_string.replace(letter, "");
        return answer;

    }
    public static void main(String[] args) {
        System.out.println(solution("abcdefg", "g"));
    }
}
