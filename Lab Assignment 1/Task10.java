/// Task__10///
import java.util.ArrayList;
public class Task10 {
    public static void main(String[]args){
        int Carray1 [] = {40,50,0,0,0,10,20,30};
        int Carray2 [] = {10,20,5,0,0,0,0,0,5,40,15,25};
        int start1 = 5;
        int size1 =  5;
        int start2 = 8;
        int size2 = 7;
        Intersection(Carray1,Carray2,start1,start2,size1,size2);

    }

    public static void Intersection(int[] Carray1, int[] Carray2, int start1, int start2, int size1, int size2) {
        int t1[] = new int [size1];
        int l=0;  
        int l2=0;  
        for (int i=0;i<size1;++i){   
              
            if(start1<Carray1.length)  { /// For Carray1//
            t1[i] = Carray1[start1];
            start1 = start1+1; 
        }
        else {
            
            t1 [i]= Carray1[0+l];
            l = l+1;
        }
        }
        
        int t2[] = new int [size2];
        for (int i=0;i<size2;++i){ 
               
            if(start2<Carray2.length)  { /// For Carray1//
            t2[i] = Carray2[start2];
            start2 = start2+1; 
        }
        
        else {
              
            t2[i]= Carray2[0+l2];
            l2 = l2+1;
        }
}
        ArrayList<Integer> n=new ArrayList<Integer>();
        int c = 0;
        for(int i=0;i<t2.length;i++){
            int q = t2[i];
            for(int j=0;j<t1.length;j++){
                if(q==t1[j]){
                   n.add(t1[j]);
                    c = c+1;
                }
            }
        }
        
            System.out.print(n);
}
}