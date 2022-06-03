import java.util.*;

class Chef_and_Chocolates{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        while(T-- > 0){
            int X = scanner.nextInt();
            int Y = scanner.nextInt();
            int Z = scanner.nextInt();

            int ans = (X*5 + Y*10) / Z;
            System.out.println(ans);
        }

    }
}