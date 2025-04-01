class Solution { // 숫자찾기
    public static int solution(int num, int k) {
       
        String n = String.valueOf(num);
        String ks = String.valueOf(k);

        int answer = n.indexOf(ks);


        return answer < 0 ? -1 : answer + 1 ;


        }
       public static void main(String[] args) {
            System.out.println(solution(29183, 1));
       }
    }
