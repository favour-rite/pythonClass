desert = (input ("Please Your Order!!! \n Ice-cream Menu \n 1. Ice-cream \n 2. Sundae \n 3. Shake "))
		
match desert:
		
	case 1: 
		icecream  = int (input (" Enter flavor selection \n 1. Chocolate \n 2. Vanila  \n 3. Strawberry "))

	
		match icecream:

			case 1:
				print (" Chocolate ")
			case 2:
				print (" Vanila ")
			
			case 3:
				print (" Strawberry ")
			

	case 2: 
		sundea = int(input (" Enter flavor selection \n 1. Chocolate \n 2. Vanila  \n 3. Strawberry "))
					
		match sundea:
		
			case 1:
				print(" Chocolate ")
			
			case 2:
				print(" Vanila ")
			
			case 3:
				print(" Strawberry ")
			
	case 3: 
		shake = int(input (" Enter flavor selection \n 1. Chocolate \n 2. Vanila  \n 3. Strawberry "))
			

		match shake:
			case 1:
				print(" Chocolate ")
			
			case 2:
				print(" Vanila ")
			
			case 3:
				print(" Strawberry ")
		
		

