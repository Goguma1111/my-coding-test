class Solution { // 숫자비교하기
    public static int solution(int num1, int num2) {
        int answer = 0;
        answer = num1 == num2 ? 1 : -1;
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(2, 3));
        System.out.println(solution(11, 11));
        System.out.println(solution(7, 99));
    }
}