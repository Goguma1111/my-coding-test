class Solution { // k의 개수
    public static int solution(int i, int j, int k) {
        int answer = 0;

        String target = String.valueOf(k); 
        
        for (int num = i; num <= j; num++) {
            String strNum = String.valueOf(num); 
            
            for (char ch : strNum.toCharArray()) { 
                if (String.valueOf(ch).equals(target)) {
                    answer++;
                }
            }
        }
        
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(1, 13, 1)); 
}
}