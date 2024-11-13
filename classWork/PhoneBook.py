print = (input (Enter menu ))

match(menu):
	
match 1: print (Phonebook)
match(Phonebook)



print("Welcome to your Nokia phone\n List of menu functions\n1 ->Phone book\n 2->Messages\n 3->Chat\n 4->Call register\n 5->Tones\n 6->Settings\n 7->Call divert\n 8->Games\n 9->Calculator\n 10->Reminders\n 11->Clock\n 12->Profiles\n 13->SIM services\n ")

print("menu")

		
choice =(input ("Enter a number"))


match (choice) 
case 1:
print("Phone book\n 1: Search\n 2: Service Nos.\n 3: Add name\n 4: Erase\n 5: Edit\n 6: Assign tone\n 7: Send b'card\n 8: Options\n 9: Speed dials\n 10: Voice tags ")

print("phone book")
phone_book = (input ("Enter a number:")
  


match (Phonebook) 
	case 1:
		print("1:Search"): 
			break:
	case 2:
		print("2:Service Nos"):
			 break:
	case 3:
		print("3:Add Name"):
			 break:
	case 4:
		print("4:Erase"):
			break:
	case 5:
		print("5:Edit"):
			 break:
	case 6:
		print("6:Assign Tone"):
			 break:
	case 7:
		print("7:Send b'card"):
			break:
	case 8:
		print("Options\n input an option\n 1. Types of view\n 2. Memory status"):
	
			
			switch(Options):
		case 1:
		print("Types Of View")
			 break:
		case 2:
		print("Memory Status"):
			 break:
			
			break:
	case 9:
		print("Speed Dials"): 
			break:
	case 10:
		print("Voice Tags"):
			break:

	default: print(" Invalid "):
			break:

		
		
			break:
	match 2:
print("Messages\n1:Write messages\n2:Inbox\n3:Outbox\n4:Picture messages\n5:Templates\n6:Smileys\n7:Message settings\n8:Info service\n9:Voice mailbox number\n10:Service command editor")

print("messsages"):

print("Input a number):

match (Messages):

	case 1:
		print("Write messages"):
		
	case 2:
		print("Inbox"):
			
	case 3:
		print("Outbox"):
		
	case 4:                                    
		print("Picture messages"):
		
	case 5:
		print("Templates"):
			
	case 6:
		print("Smileys"):
			 
	case 7:
print("Message settings") 
print("input a number")
print("1.Set 1")
print("2.Common")



match(MessagesSettings):
	case 1:
print("Input an Options:"):
print("1.Message Centre Number");
print("2.Message Sent As");
print("3.Message Validity");

switch(menumapnumber):
	case 1:	
		print("Message Centre Number"):
		
	case 2:
		print("Message Sent As"):
			
	case 3:
		print("Message Validity"):

	case 2:
		print("Common"):
		print("Input a number:"):
		print("1.Delivery Reports"):
		print("2.Reply Via Same Centre"):
		print("3.Character Support"):


		switch (menumapnumber2) 
	case 1:	
		print("Delivery Reports"):
		
	case 2:
		print("Reply Via Same Centre"):
		
	case 3:
		print("Character Support"):
			


			
}
			

	case 8:
		print("Info sevice")

	case 9:
		print("Voice mailbox number")
			
	case 10:
		print("Service command editor")
		
		default: print(" Invalid ")
}
		
	

	case 3:
		print("Chat");
		
		
	case 4:
		print(" call register/n 1: missed calls/n 2: received calls/n 3: Dialled number/n 4: Erase recent call lists/n 5: Show call duration/n 6: Show call costs/n 7: call cost settings/n 8: prepaid credit ");

	print("callregister")
	print("Input a number:")
	

	switch (callregister) {

		case 1:	
		    	 print("missed calls");
		case 2:
			print("received calls");
				
		case 3:
			print("dialled numbers");
		case 4:
			print("erase recent call lists");

		case 5:
			print("1. last call duration/n 2. All calls'duration/n 3. Received calls'duration/n 4. dialled calls duratio/n  5. clear timers ");

		print("Call duration");
	
		print("Input a number");
	

	switch (showcallduration) {

		case 1:	
			print("last call duration");
			
		case 2:
			print("all calls'duration");
			
		case 3:
			print("received calls 'duration");
				
		case 4:
			print("dialled calls'duration");
				
		case 5:
			print("clear timers");
						
}
				
		case 6:
			print(" last call cost/n 2. All calls'cost /n3. Clear counters ");

	print("call cost");
	print("Input a number");
	
	switch (ShowCallCost) {
	
		case 1: 
			print("Last call cost");
				
		case 2:
			print("All calls'cost");
		case 3:
			print("Clear counters");
}
				break;
		case 7: 
			print("call costs settings\n 1.call cost limit\n 2.show costs in");
	print("cost settings");
	print("Input a number");
		switch (CallCostSettings) {

		case 1:
			print("1:Call cost limit")
			
		case 2:
			print("2:Show costs in")
}
		case 8:
			print("3:Prepaid credit")

		default: System.out.print(" Invalid ")
			
}
		
} switch (choice) {
    case 5:
     	print("Tones");
        print("1. Ringing tone\n 2. Ringing volume\n 3. Incoming call alert\n 4. Composer\n 5. Message alert tone\n 6. Keypad tones\n 7. Warning and game tones\n 8. Vibrating alert\n 9. Screen saver");

        Scanner tone = new Scanner(System.in);
        System.out.println("Input a number");
        int tones = tone.nextInt();
        switch (tones) {
            case 1:
                System.out.println("Ringing tone");
                break;
            case 2:
                System.out.println("Ringing volume");
                break;
            case 3:
                System.out.println("Incoming Call Alert");
                break;
            case 4:
                System.out.println("Composer");
                break;
            case 5:
                System.out.println("Message Alert Tone");
                break;
            case 6:
                System.out.println("Keypad Tones");
                break;
            case 7:
                System.out.println("Warning And Game Tones");
                break;
            case 8:
                System.out.println("Vibrating Alert");
                break;
            case 9:
                System.out.println("Screen Saver");
                break;
        }
        break;
    case 6:
        System.out.println("Call Settings");
        System.out.println("1. Automatic redial\n 2. Speed dialling\n 3. Call waiting options\n 4.Own number sending\n 5. Phone line in use\n 6. Automatic answer");

        Scanner caller = new Scanner(System.in);
        System.out.println("Input a number");
        int call = caller.nextInt();
        switch (call) {
            case 1:
                System.out.println("Automatic redial");
                break;
            case 2:
                System.out.println("Speed dialling");
                break;
            case 3:
                System.out.println("Call waiting options");
                break;
            case 4:
                System.out.println("Own number sending");
                break;
            case 5:
                System.out.println("Phone line in use");
                break;
            case 6:
                System.out.println("Automatic answer");
                break;
        }
        break;
    case 7:
        System.out.println("Call divert");
        break;
    case 8:
        System.out.println("Games");
        break;
    case 9:
        System.out.println("Calculator");
        break;
    case 10:
        System.out.println("Reminder");
        break;
	default: System.out.print(" Invalid ");
		break;

    case 11:
        System.out.println("Clock");
        System.out.println("1. Alarm clock\n 2. Clock settings\n 3. Date setting\n 4. Stopwatch\n 5. Countdown timer\n 6. Auto update of date and time");

        Scanner alarm = new Scanner(System.in);
        System.out.println("Input a number");
        int clock = alarm.nextInt();

        switch (clock) {
            case 1:
                System.out.println("Alarm Clock");
                break;
            case 2:
                System.out.println("Clock Setting");
                break;
            case 3:
                System.out.println("Date Setting");
                break;
            case 4:
                System.out.println("Stopwatch");
                break;
            case 5:
                System.out.println("Countdown Timer");
                break;
            case 6:
                System.out.println("Auto update of date and time");
                break;
	   default: System.out.print(" Invalid ");

        } 
        break;
    case 12:
        System.out.println("Profiles");
        break;
    case 13:
        System.out.println("Sim Services");
        break;
		}
	}
}