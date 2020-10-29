
import java.util.Scanner;    
public class InstallJava{
    public static void main(String[] args) {
        System.out.println("enter the string");
        Scanner s=new Scanner(System.in);
        String str=s.nextLine();
        char name[] = str.toCharArray();  
        for(int i=0;i<=name.length-2;i++){
            for(int j=i+1;j<=name.length-1;j++){
                if(name[i]==name[j]){
                    System.out.println(" not unique"); 
                    System.exit(0);
                }     
                
            }
            
            
        }
        System.out.println("unique");
         

            
    }
}   

