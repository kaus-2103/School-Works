/// Task__4///
import java.util.Scanner;
public class Task4 {
    public static void main(String []args){
        int [] source = {10,2,30,2,50,2,2,0,0};
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        int size = sc.nextInt();
        System.out.print("Put the element you want to remove: ");
        int k= sc.nextInt();
        removeAll(source,size,k);
        sc.close();
    }
    public static void removeAll(int [] source,int size, int k){
        int source2 [] = new int [size];
        int j=0 ;
        for (int i = 0;i<size;i++){
            if(source[i]!=k){
                source2[j]= source[i]; // I want to fill an empty array without selected elements and problem is it fills up zero rather than any other number.//
                j++;
            }
        }
        for(int i=0;i<source2.length;i++){   ///java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 5///
            System.out.print(source2[i]+",");
        }

    }
}
