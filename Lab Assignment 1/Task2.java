/// Task__2///
import java.util.Scanner;
public class Task2 {
    public static void main(String []args){
        int [] source = {10,20,30,40,50,60};
        Scanner sc= new Scanner (System.in);
        System.out.print("Enter the value of k: ");
        int k=sc.nextInt();
        rotateLeft(source,k);
        sc.close();
    }
    public static void rotateLeft(int []source, int k){
        for (int i=0, j=i+k;i<k;i++,j++){
            int temp= source[i];
            source[i]=source[j];
            source[j]=temp;
        }
        for(int i=0;i<source.length;i++){
            System.out.print(source[i]+",");
        }
    }
}
