/// Task__9///
public class Task9 {
    public static void main(String []args){
        int array [] = {10,20,0,0,0,10,20,30};
        int start =  5;
        int size = 5;
        palindrome(array,start,size);
    }
    public static void palindrome(int[] array, int start, int size) {
        int array2[] = new int [size];
        int c = 0;
        for(int i=0;i<size-1;i++){
            if(start+i<array.length){
                array2[i] = array[start+i]; 
            }
            else if(start+i>array.length-size){
                array2[i] = array [i];
                c = c+1;
            }
            else{
                break;
            }
        }
        int f = 0;
        int r = array2.length-1;
         int c2= 0;
        for (int i = 0;i<array2.length;i++){
            if (array2[f]==array2[r]){
                c2 = c2+1;
            }
            else {
                break;
            }
            f = f+1;
            r = r-1;
        }
        if (c2==size){
            System.out.print("True");
        }
        else{
            System.out.print("False");
        }
    }
}
