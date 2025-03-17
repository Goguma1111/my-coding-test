class Solution { // 대문자로 바꾸기
    public static String solution(String myString) {
        String answer = myString.toUpperCase();
        return answer;
    }


    public static void main(String[] args) {

        System.out.println(solution("abcDEFG"));

    }
}