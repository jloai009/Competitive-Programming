import java.util.*;

class Chef_and_Brain_Speed{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int X = scanner.nextInt();
        int Y = scanner.nextInt();
        String ans = Y > X ? "YES" : "NO";
        System.out.println(ans);
    }
}