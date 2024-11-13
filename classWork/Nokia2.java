import  java.util.Scanner;

public class Nokia2{
	public static void main (String[] args){


		Scanner input =new Scanner (System.in);
		System.out.print("Enter your choice/n to exit ");
		int choice = input.nextInt();

		switch(choice){
		case 1 : 	System.out.print("Phonebook"); 
				int phonebook = input.nextInt();
				switch(phonebook) {

				case 1 : System.out.print(" Search "); 
								break;
				case 2 : System.out.print(" Service "); 
								break;
				case 3 : System.out.print(" Add name "); 
								break; 
				case 4 : System.out.print(" Erase ");
								 break;
				case 5 : System.out.print(" Edit "); 		
								 break;
				case 6 : System.out.print(" Assign tone ");
								 break;
				case 7 : System.out.print(" Send b' card ");
								 break;
			} 	
					break;


				case 8 : System.out.print(" options ");
					int options = input.nextInt();
					switch(options){
					
					case 1:System.out.print(" Type of view "); 	
									break;
					case 2:System.out.print(" Memory status "); 								
									break;
					}
					
					break;


				case 9: System.out.print(" Speed dials "); 
								break;
				case 10: System.out.print(" Voice tags "); 
								break;
					