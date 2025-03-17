class Solution {
    public static int solution(int num, int n) {
        int answer = 0;

        answer = num % n == 0 ? 1 : 0;

        return answer;

    
        
    }
    public static void main(String[] args) {
        System.out.print(solution(34, 3));
    }
}