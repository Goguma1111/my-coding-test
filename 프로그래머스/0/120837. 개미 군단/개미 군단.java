class Solution { // 개미군단
    public static int solution(int hp) {
        int answer = 0;

        answer += (hp / 5);
            hp %= 5;

        answer += (hp / 3);
            hp %= 3;
            
        answer += (hp / 1);    
        
        return answer;    
    }


    public static void main(String[] args) {
        System.out.println(solution(23));
        System.out.println(solution(24));
    }
} 