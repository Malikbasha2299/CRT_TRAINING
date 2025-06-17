public class VowelsAndConsonents{
 public static void main(String[] args){
  
   String name = new String("apple");
   int length = name.length();
   int vowels = 0;
   int consonents = 0;
   for(int i=0; i<length; i++){
   char character = name.charAt(i);
   if(character =='a' || character == 'e' || character == 'i' || character == 'o' || character == 'u'){
       vowels++;
       
   }
   else{
       consonents++;
   }
}
System.out.println("no of vowels ="+vowels);
System.out.println("no of consonents ="+consonents);

}
}
