/// Task__6///
import java.util.Scanner;
public class Task6 {
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the value of the n: ");
        int n=sc.nextInt();
        Arrayseries(n);
        sc.close();
    }
    public static void Arrayseries(int n){
        int array[] = new int[n*n];
        int l = array.length-1;
        for(int i=array.length-1;i>0;i--){
            int t1 = 1;
            int t= n;
            int t2 = t;
            int t3 = 0;
            for (int j=0;j<=3;j++){
                array[l-t3] =t2;
                if(t2>0){
                t2 = t2 - 1;
                }
                else{
                    t2=0;
                }
                t3 = t3 +1;
            }
            t = t-1;
            t1 = n - t1;
           
        }
        for(int i=0;i<array.length;i++){
            System.out.print(array[i]+",");
        }
    }
}
