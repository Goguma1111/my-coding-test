class Solution {
    public static int solution(int n) {
        int answer = 0;
        if (n % 7 != 0) {
            return  answer = n/7+1;
        } else {
            answer =  n/7;
        }
        return answer;
    }
    public static void main(String[] args) {
        System.out.println(solution(7));
        System.out.println(solution(1));
        System.out.println(solution(15));
    }
}