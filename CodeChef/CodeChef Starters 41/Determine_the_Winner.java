import java.util.*;

class Determine_the_Winner{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        while(T-- > 0){
            int PA = scanner.nextInt();
            int PB = scanner.nextInt();
            int QA = scanner.nextInt();
            int QB = scanner.nextInt();
            int P_time = Math.max(PA, PB);
            int Q_time = Math.max(QA, QB);
            String ans = "TIE";
            if(P_time < Q_time){
                ans = "P";
            }else if(P_time > Q_time){
                ans = "Q";
            }
            System.out.println(ans);
        }
    }
}