import java.util.Scanner;
public class ReversedArraySwap {
    public static void main(String[] args) {
          Scanner sc = new Scanner(System.in);
          System.out.print("size = ");
        int size = sc.nextInt();
        int []array = new int[size];
    
              for(int i=0; i<size; i++){
            array[i] = sc.nextInt();
    
        }
        int left = 0;
       int right = size-1;
     
       while(left<right){
           int value = array[left];
           array[left] = array[right];
           array[right] = value;
            left++;
            right--;
           
       }
        
        System.out.println("-------------------------------------");
        for(int i=0; i<size; i++){
            System.out.println(array[i]);
        }
    }
}