department = int(input("Enter your departmnt  \n 1. IT \n 2. HR \n 3. FINANCE \n "))
		

match department:

	case 1:
		IT = int(input (" Enter your sub-department \n 1. Manager \n 2. Analyst \n 3. Imtern "))		
		
		match IT:

			case 1:
				print(" Manager ")
		
			case 2: 
				print(" Analyst ")
		
			case 3:	
				print(" Intern ")
		


	case 2:
		hR = int(input (" Enter your sub-department  \n 1. Manager \n 2. Analyst \n 3. Imtern "))	

		match hR:


			case 1:
				print(" Manager ")
			

			case 2:
				print(" Analyst ")
		

			case 3:
				print(" Intern ");
		
	case 3:
		finance = int(input (" Enter your sub-department  \n  1. Manager \n 2. Analyst \n 3. Imtern "))

		match finance:
		
			case 1:
				print(" Manager ")
		
			case 2:
				print(" Analyst ")
			
			case 3:
				print("Intern ")
		

