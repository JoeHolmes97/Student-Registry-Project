
# Module for registering students

def RegStudents(o_StudentList): # Function for registering students

    bContinue = True # Set bContinue to True

    while bContinue == True: # While bContinue is True, loop

        print("\n----------------Register Student Menu----------------\n")

        s_MenuItems = ["Please choose an option: ", "Add New Student", "Exit"] # Create a list of menu options

        sUserInput = GenFun.Menu(s_MenuItems) # Run the dynamic menu function and assign the returned result to sUserInput

        if sUserInput == "1": # If the user enters 1, do this

            s_InputDetails = ["","",""] # Create a blank list with 3 entries

            bLoop = True # Create a variable for exiting a loop

            while bLoop == True: # While bLoop is True, do this

                s_InputDetails[0] = input("Please enter the students first name: ") # Asks the user for a first name
                s_InputDetails[1] = input("Please enter the students last name: ") # Asks the user for a last name

                bAge = False # Set bAge to false (representing that the age entered was invalid)
                while bAge == False: # While bAge is false, loop

                    try: # Try this, if an error occurs, raise an exception
                        s_InputDetails[2] = int(input("Please enter the students age: ")) # Asks the user for the students age

                        if s_InputDetails[2] < 16 or s_InputDetails[2] > 120: # If iAge is outside the age boundaries, do this
                            raise Cls.ValueOutOfRange # Raise the ValueOutOfRange error

                    except Cls.ValueOutOfRange: # If the ValueOutOfRange error is raised, do this
                        print("The age entered needs to be between 16 and 120, please try again")

                    except ValueError: # If the 'ValueError' error is raised, do this
                        print("Please enter a valid whole number")

                    except: # If an error that not included above occurs, do this
                        print("Unkown Error occured, please try again")

                    else: # If there are no errors, do this
 
                        print("First Name: " + s_InputDetails[0] + "\nLast Name: " + s_InputDetails[1] + "\nAge: " + str(s_InputDetails[2]))

                        s_MenuItems = ["Are you happy with these details?", "Yes", "No"] # Create a list of menu items
                        sUserChoice = GenFun.Menu(s_MenuItems) # Run the dynamic menu function using the menu items, and assign the returned value to sUserChoice

                        if sUserChoice == "1": # If the user enters 1, do this
                            
                            o_StudentList.append(Cls.Student(s_InputDetails[0], s_InputDetails[1], s_InputDetails[2])) # Create a Student object with the attributes entered (first
                            # name, last name and age) and append the object to the end of o_StudentList
   

                            bAge = True
                            bLoop = False # Set bLoop to False, exiting the loop
                        elif sUserChoice == "2":
                            print("Please enter the details again")

                            bAge = True     
                                    
        elif sUserInput == "2":
            print("Returning to previous menu")
            bContinue = False            
            return o_StudentList
