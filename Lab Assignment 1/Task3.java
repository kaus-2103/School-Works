/// Task__3///
import java.util.Scanner;
public class Task3 {
    public static void main(String []args){
        Scanner sc= new Scanner(System.in);
        int []source = {10,20,30,40,50,0,0};
        System.out.print("The number of the Index you want to remove: ");
        int idx = sc.nextInt();
        System.out.println("");
        System.out.print("The size of the Array: ");
        int size = sc.nextInt();
        remove(source,size,idx);
        sc.close();
    }
    public static void remove(int []source,int size, int idx){
        for (int i= idx;i<size-1;i++){
             int temp = source[i+2];
             source[i] = source[i+1];
             source[i+1] = temp;

        }
        for(int i=0;i<source.length;i++){
            System.out.print(source[i]+",");
        }
    }
}
