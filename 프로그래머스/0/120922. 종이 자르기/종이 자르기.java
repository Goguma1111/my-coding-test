    class Solution {    // 종이 자르기
        public static int solution(int M, int N) {

            int answer = (M-1) + M * (N-1);
            return answer;

        }

        public static void main(String[] args) {
            System.out.println(solution(2, 2));
            System.out.println(solution(2, 5));
            System.out.println(solution(1, 1));
        }
    }   