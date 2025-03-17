class Solution { // rny_string
    public static  String solution(String rny_string) {
        String answer = rny_string.replace("m","rn");
        return answer;
    }


    public static void main(String[] args) {
        System.out.println(solution("masterpiece"));
    }
}

