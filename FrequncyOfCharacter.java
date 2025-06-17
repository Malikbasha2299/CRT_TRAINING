import java.util.Scanner;
public class FrequncyOfCharacter {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        System.out.print("enter the name :");
        String name = sc.nextLine();
        int length = name.length();
       char []array = new char[length];
       char []reverse = new char[length];
       for(int left =0 ; left<length ; left++){
           array[left] = name.charAt(left);
       }
       int count = 0;
    
       for(int left=0 ; left<length; left++){
       count = 1;
           for(int right= left+1 ; right<name.length()  ; right++){
               if(array[left]=='_'){
                   continue;
               }
               else if(array[left] == array[right]){
                   count++;
                   array[right] ='_';
               }
           }
           if(array[left] !='_'){
               System.out.println(array[left]+" = "+count);
           }
           
       }
    }
}