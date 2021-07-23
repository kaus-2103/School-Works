/// Task__1///
import java.util.Scanner;
public class Task1{
    public static void main(String [] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the index of array: ");
        int n = sc.nextInt();
        int a[] = new int[n];
        System.out.println("Enter the elements of array: ");
        for (int i = 0;i<n;i++){
            int l=sc.nextInt();
            a[i]=l;
        }
        System.out.println("Enter the index from where you want to shift: ");
        int k=sc.nextInt();
        shiftLeft(a, k);
        sc.close();
        }
    public static void shiftLeft (int[] source, int k) {
        for(int i=0;i<source.length;i++){
            int j=i+k;
            if(i<k){    // only works in middle number. Problem: Index __ out of bounds for lengths //
                source[i]=source[j];
            }
            else{
                source[i]=0;
            }
        }
        for(int i=0;i<source.length;i++){
            System.out.print(source[i]+",");

}
}
}