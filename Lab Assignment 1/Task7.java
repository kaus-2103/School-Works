/// Task__7///
public class Task7 {
    public static void main(String []args)
    {
        int array[] = {1,1,2, 2, 1, 1,1,1};
        maxBunch(array);
    }
    public static void maxBunch(int array []){
        int temp = 0;
        int max= 0;
        for (int i=0;i<array.length-1;i++){
        temp = array[i];
        int count = 2;
        for(int j=i+1;temp==array[j]&&j<array.length-1;++j){
             count=count+1;
             
            }
            if(count>max){
                max = count;
            }
        }
        System.out.print(max);
        }
    }