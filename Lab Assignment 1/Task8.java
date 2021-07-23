/// Task__8///
import java.util.ArrayList;
public class Task8 {
    public static void main(String []args){
        int source[] = {4,5,6,6,4,3,6,4};
        repetition(source);
    }
    public static void repetition(int [] source){
        ArrayList<Integer> n=new ArrayList<Integer>();
        int t = 0;
        for (int i = 0; i< source.length;i++){
            int count = 0;
            for (int j=0;j<source.length;j++){
                if(source[i]==source[j]){
                    count = count+1;
                    t= t+1;
                }
            }
          n.add(count);
        }
        int count2 = 0;
        for(int i=0;i<t;i++){
            for(int j=i+1;j<t;j++){
                count2 = count2 +1;
            }
        }
        if (count2>0){
            System.out.print("True");
        }
        else{
            System.out.print("False");
        }
    }
}
