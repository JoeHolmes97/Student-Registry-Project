
# Week 8 Project - College registry system
#  - Dynamic menu - menu inside function
#  - Register student, assign student to class, take register, exit program
# - Inside list

# ---------------------------Classes-----------------------------

class ValueOutOfRange(Exception): # Creates a custom exception, which inherits from the exception class, called ValueOutOfRange
    pass # Do nothing

class Student: # Class for students
    sFirstName = "" # Create some member attributes to define the object
    sLastName = ""
    iAge = 0
    sClassName = ""
    bAttendance = False

    def __init__(self, sFirstName, sLastName, iAge): # Constructor used to initialise the student objects with data provided by the user
        self.FirstName = sFirstName
        self.LastName = sLastName
        self.Age = iAge
        # self.Class = sClassName
        #self.Attendance = bAttendance

    def PrintDetails(self): # Member function for printing the attributes of the object
        print(self.FirstName, self.LastName, self.iAge, self.bAttendance)

class Class: # Create a class called Class
    sClassName = "" # Create a variable inside the class

    def __init__(self): # Initialise the variables
        self.Class = "None"

# ---------------------------Classes-----------------------------

# ---------------------------Functions-----------------------------

def LineBreak(): # Function for printing a line break
    print("\n------------------------\n")

def Menu(s_MenuItems): # Function for creating a dynamic menu

    bLoop = True # Set a variable for exiting a loop

    while bLoop == True: # While bLoop is True, loop
  
        print(s_MenuItems[0]) # Print the first item in the menu
    
        for i in range(1, len(s_MenuItems)): # Loop a number of times starting at 1 and ending at the length of the list
      
            print(str(i) + ": " + s_MenuItems[i]) # Print the number followed by the list item at that index
        sUserInput = input("--> ") # Get an input from the user

        bLoop = MenuErrors(s_MenuItems, sUserInput) # Set bLoop equal to the returned value for MenuErrors
  
    return sUserInput # Return the user input

def MenuErrors(s_MenuItems, sUserInput): # Function for errors in the dynamic menu

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

def RegStudents(o_StudentList): # Function for registering students

    bContinue = True # Set bContinue to True

    while bContinue == True: # While bContinue is True, loop

        print("\n----------------Register Student Menu----------------\n")

        s_MenuItems = ["Please choose an option: ", "Add New Student", "Exit"] # Create a list of menu options

        sUserInput = Menu(s_MenuItems) # Run the dynamic menu function and assign the returned result to sUserInput

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
                            raise ValueOutOfRange # Raise the ValueOutOfRange error

                    except ValueOutOfRange: # If the ValueOutOfRange error is raised, do this
                        print("The age entered needs to be between 16 and 120, please try again")

                    except ValueError: # If the 'ValueError' error is raised, do this
                        print("Please enter a valid whole number")

                    except: # If an error that not included above occurs, do this
                        print("Unkown Error occured, please try again")

                    else: # If there are no errors, do this
 
                        print("First Name: " + s_InputDetails[0] + "\nLast Name: " + s_InputDetails[1] + "\nAge: " + str(s_InputDetails[2]))

                        s_MenuItems = ["Are you happy with these details?", "Yes", "No"] # Create a list of menu items
                        sUserChoice = Menu(s_MenuItems) # Run the dynamic menu function using the menu items, and assign the returned value to sUserChoice

                        if sUserChoice == "1": # If the user enters 1, do this
                            
                            o_StudentList.append(Student(s_InputDetails[0], s_InputDetails[1], s_InputDetails[2])) # Create a Student object with the attributes entered (first
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

def DisplayStudents(o_StudentList): # Function to diplay all students in the o_StudentList list
       
    for i in range(0, len(o_StudentList)): # Run through the student list

        print("\nName: " + o_StudentList[i].FirstName, o_StudentList[i].LastName) # Prints the first and last name of the student
        print("Age:", o_StudentList[i].Age) # Prints the students age
                   
def AssignStudents(o_StudentList, s_Classes): # Function for assigning a student to a class

    bContinue = True

    while bContinue == True:

        DisplayStudents(o_StudentList) # Run the DisplayStudents function with the list o_StudentList

        print("\n----------------Assign Student----------------\n")

        s_MenuItems = ["Which student would you like to assign to a class?"] # Create a list with this string as the only entry

        for i in range(0, len(o_StudentList)): # Loop a number of times equal to the number of students
            s_MenuItems.append(o_StudentList[i].FirstName + " " + o_StudentList[i].LastName) # Add the first and last name of the current student to the end of the list

        s_MenuItems.append("Return to main menu") # Add this option to the end of the list

        iMenuChoice = int(Menu(s_MenuItems)) # Run the Menu function with the list s_MenuItems

        if iMenuChoice == len(s_MenuItems) - 1: # If the user chooses the last menu option, do this
            
            bContinue = False # Set bContinue to False, exiting the loop

            LineBreak()

        else:

            bLoop = True

            while bLoop == True:
                
                s_MenuItems = ["\n Which class would you like to assign " + o_StudentList[iMenuChoice-1].FirstName + " " + o_StudentList[iMenuChoice-1].LastName + " to?"]

                for x in range(0, len(s_Classes)):

                    s_MenuItems.append(s_Classes[x])

                s_MenuItems.append("Return")

                iClassChoice = int(Menu(s_MenuItems))

                if iClassChoice == len(s_MenuItems) - 1:
                    
                    bLoop = False

                else: 

                    bLoop = False

                    o_StudentList[iMenuChoice - 1].sClassName = s_Classes[iClassChoice-1]

                    print("You have successfully assigned " + o_StudentList[iMenuChoice-1].FirstName + " " + o_StudentList[iMenuChoice-1].LastName + " to " + s_Classes[iClassChoice-1])

# ---------------------------Functions-----------------------------

LineBreak()

# ---------------------------Main Program-----------------------------

print("Welcome to the college registry menu\n")

# o_StudentList = [] # Create an empty list for the Student objects ----------------Replace next line of code with this one when testing is finished

o_StudentList = [Student("Joe", "Holmes", 25), Student("Jack", "Ryan", 33), Student("James", "Cameron", 44), Student("Jill", "Valentine", 30), Student("Lyse", "Hext", 26)]
# Test data above ^
s_Classes = ["Programming", "Maths", "English", "Pyhsics", "History"]


bContinue = True # Set up a variable for exiting a loop

while bContinue == True: # While bContinue is True, loop
  
    print("\n----------------College Registry Main Menu----------------\n")

    s_MenuItems = ["Please select an option:", "Register student", "Assign a student to a class", "Take a register", "Exit the program"]
# Creates a list of menu items to use, with the possibity of adding more
    sUserInput = Menu(s_MenuItems) # Run the function Menu with the list of menu items, and assign the returned value to sUserInput

    LineBreak()

    if sUserInput == "1": # If the user enters 1, do this
    
        RegStudents(o_StudentList) # Run the RegStudents() function, and appends the returned result to o_StudentList list
        
        DisplayStudents(o_StudentList)

        LineBreak()
  
    elif sUserInput == "2": # Assign a student to a class, not coded yet
       
        AssignStudents(o_StudentList, s_Classes)

    elif sUserInput == "3":
        print("Coming soon 3") # Take a register, not coded yet

    elif sUserInput == "4": # Option for exiting the program
        print("Exiting the program")
        bContinue = False # Set bContinue to false, exiting the program

# ---------------------------Main Program-----------------------------


# To search through the list of objects for a specific person, use for loop to loop through list, comparing the values to the user input
# Use function inside the 'Class' class to add students to a list i.e add students to Class register