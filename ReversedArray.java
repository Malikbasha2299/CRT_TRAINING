import java.util.Scanner;
public class ReversedArray {
    public static void main(String[] args) {
          Scanner sc = new Scanner(System.in);
          System.out.print("size = ");
        int size = sc.nextInt();
        int []array = new int[size];
        int []reversed = new int[size];
      
        for(int i=0; i<size; i++){
            array[i] = sc.nextInt();
            
        }
        int j = 0;
        for(int i = size-1 ; i>=0; i--){
        reversed[j] = array[i];
        j++;
        }
        
        System.out.println("-------------------------------------");

        for(int i=0; i<size; i++){
            System.out.println(reversed[i]);
        }
    }
}