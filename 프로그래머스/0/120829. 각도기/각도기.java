class Solution { // 각도기
    public static int solution(int angle) {
        int answer = 0;
        if (0 < angle && angle <90) {
            return answer = 1;
        } 
        else if(angle == 90) {
            return answer = 2;
        }
         else if (90 < angle && angle < 180) {
            return answer = 3;
        }
         else {
            return answer = 4;
        }

    }
    public static void main(String[] args) {
        System.out.println(solution(70));
        System.out.println(solution(91));
        System.out.println(solution(180));
    }
}