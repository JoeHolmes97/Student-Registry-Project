
# Week 8 Project - College registry system
#  - Dynamic menu - menu inside function
#  - Register student, assign student to class, take register, exit program
# - Inside list

# ---------------------------Classes-----------------------------

class ValueOutOfRange(Exception): # Creates a custom class, which inherits from the exception class, called MenuOutOfRange
    pass # Do nothing

class Student: # Create a class called student
    sFirstName = "" # Create some member attributes to define the object
    sLastName = ""
    iUserAge = 0
    bAttendance = False

    def __init__(self, sFirstName, sLastName, iUserAge): # Constructor used to initialise the student objects with data provided by the user
        self.FirstName = sFirstName
        self.LastName = sLastName
        self.UserAge = iUserAge
        #self.Attendance = bAttendance

    def PrintDetails(self):
        print(self.FirstName, self.LastName, self.iUserAge, self.bAttendance)

class Class: # Create a class called Class
    sClassName = "" # Create a variable inside the class

    def __init__(self): # Initialise the variables
        self.Class = "None"

# ---------------------------Classes-----------------------------

# ---------------------------Functions-----------------------------

def LineBreak(): # Function for printing a line break
    print("\n------------------------\n")

def Menu(s_MenuItems): # Create a function called Menu which accepts 1 argument

    bLoop = True # Set a variable for exiting a loop

    while bLoop == True: # While bLoop is True, loop
  
        print(s_MenuItems[0]) # Print the first item in the menu
    
        for i in range(1, len(s_MenuItems)): # Loop a number of times starting at 1 and ending at the length of the list
      
            print(str(i) + ": " + s_MenuItems[i]) # Print the number followed by the list item at that index
        sUserInput = input("--> ") # Get an input from the user

        bLoop = MenuErrors(s_MenuItems, sUserInput) # Set bLoop equal to the returned value for MenuErrors
  
    return sUserInput # Return the user input

def MenuErrors(s_MenuItems, sUserInput): # Create a function called MenuErrors that accepts exactly 2 arguments

    try: # Starts the try-except

        iUserInput = int(sUserInput) # Try to convert the user input into an integer
    
        if iUserInput > len(s_MenuItems) - 1 or iUserInput < 1: # If the user entered a number outside of the numbers in the list, do this
            raise ValueOutOfRange # Raise the custom exception

    except ValueOutOfRange: # If the custom exception MenuOutOfRange is raised, do this
        print("\nPlease only enter a valid number from the list provided")
        input("[Press enter to try again]") # Ask the user to press enter to continue, to make sure they saw the message

    except ValueError: # If the ValueError error is raised, do this
        print("\nPlease input a valid whole number")
        input("[Press enter to try again]")

    except: # If an error occurs that wasn't one of the above errors, do this
        print("\nAn unkown error occurred, please try again")
        input("[Press enter to try again]")

    else: # If no errors are raised, do this
        return False # Return the value False

def RegStudents():

    bContinue = True

    while bContinue == True:

        s_MenuItems = ["Please choose an option: ", "Add New Student", "Exit"]

        sUserInput = Menu(s_MenuItems)

        if sUserInput == "1":

            s_InputDetails = ["","",""]

            bLoop = True # Create a variable for exiting a loop

            while bLoop == True: # While bLoop is True, do this

                s_InputDetails[0] = input("Please enter the students first name: ") # Asks the user for a first name
                s_InputDetails[1] = input("Please enter the students last name: ") # Asks the user for a last name

                bAge = False
                while bAge == False:

                    try:
                        s_InputDetails[2] = int(input("Please enter the students age: ")) # Asks the user for the students age

                        if s_InputDetails[2] < 16 or s_InputDetails[2] > 120: # If iAge is outside the age boundaries, do this
                            raise ValueOutOfRange # Raise the ValueOutOfRange error

                    except ValueOutOfRange: # If the ValueOutOfRange error is raised, do this
                        print("The age entered needs to be between 16 and 120, please try again")

                    except ValueError: # If the 'ValueError' error is raised, do this
                        print("Please enter a valid whole number")

                    except: # If an error that not included above occurs, do this
                        print("Unkown Error occured, please try again")

                    else: # If there are no errors, do this
 
                        print("First Name: " + s_InputDetails[0] + "\nLast Name: " + s_InputDetails[1] + "\nAge: " + str(s_InputDetails[2]))

                        s_MenuItems = ["Are you happy with these details?", "Yes", "No"]
                        sUserChoice = Menu(s_MenuItems)

                        if sUserChoice == "1":
                            
                            o_StudentList.append(Student(s_InputDetails[0], s_InputDetails[1], s_InputDetails[2]))

                            bAge = True
                            bLoop = False # Set bLoop to False, exiting the loop
                        elif sUserChoice == "2":
                            print("Please enter the details again")

                            bAge = True
       

        
        elif sUserInput == "2":
            print("Returning to previous menu")
            bContinue = False            
            return o_StudentList
        

# ---------------------------Functions-----------------------------

LineBreak()

# ---------------------------Main Program-----------------------------

print("Welcome to the college registry menu\n")

o_StudentList = [] # Create an empty list for the Student objects

bContinue = True # Set up a variable for exiting a loop

while bContinue == True: # While bContinue is True, loop
  
    s_MenuItems = ["Please select an option:", "Register student", "Assign a student to a class", "Take a register", "Exit the program"]
# Creates a list of menu items to use, with the possibity of adding more
    sUserInput = Menu(s_MenuItems) # Run the function Menu with the list of menu items, and assign the returned value to sUserInput

    LineBreak()

    if sUserInput == "1": # If the user enters 1, do this
    
        o_StudentList.append(RegStudents())

        LineBreak()
  
    elif sUserInput == "2":
        print("Coming soon 2")

    elif sUserInput == "3":
        print("Coming soon 3")

    elif sUserInput == "4": # Option for exiting the program
        print("Exiting the program")
        bContinue = False # Set bContinue to false, exiting the program

# ---------------------------Main Program-----------------------------


# To search through the list of objects for a specific person, use for loop to loop through list, comparing the values to the user input
# Use function inside the 'Class' class to add students to a list i.e add students to Class register