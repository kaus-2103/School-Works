import java.util.Scanner;
public class Test{
    public static void main(String[] args) {
        Scanner sc=new Scanner (System.in);
        int l =sc.nextInt();
        int t = testmethod(l);
        System.out.print(plustestmethod(t));
        sc.close();
    }
     int plustestmethod(int p) {
        p = p+1;
        return p;
    }
    public static int testmethod(int a) {
        return a;
        
    }
}