class Solution { //공배수 구하기
    public static int solution(int number, int n, int m) {
        int answer = 0;
        answer = number % n == 0 && number % m==0 ? 1 : 0; //삼항연산자
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(60, 2, 3));
        System.out.println(solution(55, 10, 5));
    }
}