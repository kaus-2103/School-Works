/// Task__5///
import java.util.Scanner;
public class Task5 {
    public static void main(String [] args){
        Scanner sc = new Scanner (System.in);
        System.out.print("Enter the index of array: ");
        int n = sc.nextInt();
        int source[] = new int[n];
        System.out.println("Enter the elements of array: ");
        for (int i = 0;i<n;i++){
            int l=sc.nextInt();
            source[i]=l;
        }
        Arraysorting(source);
        sc.close();
    }
    static void Arraysorting(int source[]){
       int temp = 0;
       int temp2 = 0;
       int count = 0;
       for(int i = 1;i<source.length;i++){
           for(int j=0;j<i;j++){
               temp += source[j];
           }
           for(int k=i;k<source.length;k++){
               temp2 +=source[k];
           }
           if(temp == temp2){
               count = count+1;
           }
           else{
               temp = 0;
               temp2 = 0;
           }
       } 
       if(count == 1){
        System.out.print("True.");
       }
       else{
           System.out.print("False");
       }
    }
}
