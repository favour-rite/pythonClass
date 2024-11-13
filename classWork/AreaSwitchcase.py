area = (input("Enter the Area of different shapes you want to calculate \n 1. Circle \n 2. Rectangle \n 3. Triangle "))
	
		
match area:
	case 1:
		circle = int (input (" Enter to solve the ara of a circle "))
					
		match circle:
		
		
			case 1:
				radius = int(input(" Enter to solve the following \n  1. Radius for cicle \n 2. length and breadth \n 3. breadth and height "))					
				pi = 3.42

				result =  pi * radius * radius
				print (result)
		
				
	case 2: 
		rectangle =int (input(" Enter to solve the following \n  1. Radius for cicle \n 2. length and breadth \n 3. breadth and height "))					  
			
		match rectangle :
			case 1:
				length = (input(" Enter length "))
						
				breath = (input(" Enter breath1 "))
					
				areaofrectangle =  length1 * breath
				print ( areaofrectangle )
			


	case 3:

		triangle =int (input (" Enter to solve the following \n  1. Radius for cicle \n 2. length and breadth \n 3. breadth and height "))					
				
	
		match triangle:
			

			case 1: 
				breadth = (input(" Enter Breath"))
				height = (input(" Enter height "))
	
				half = 0.5;

				areaoftriangle = half * breath * height

				print (areaoftriangle)

					
				
				







		




	


