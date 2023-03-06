
# Week 8 Project - College registry system
#  - Dynamic menu - menu inside function
#  - Register student, assign student to class, take register, exit program
# - Inside list

import Register_Classes as Cls
import Generic_Functions as GenFun

# ---------------------------Classes-----------------------------



# ---------------------------Classes-----------------------------

# ---------------------------Functions-----------------------------

def LineBreak(): # Function for printing a line break
    print("\n------------------------\n")



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

        iMenuChoice = int(GenFun.Menu(s_MenuItems)) # Run the Menu function with the list s_MenuItems

        if iMenuChoice == len(s_MenuItems) - 1: # If the user chooses the last menu option, do this
            
            bContinue = False # Set bContinue to False, exiting the loop

            LineBreak()

        else:

            bLoop = True

            while bLoop == True:
                
                s_MenuItems = ["\n Which class would you like to assign " + o_StudentList[iMenuChoice-1].GetName() + " to?"]

                for x in range(0, len(s_Classes)):

                    s_MenuItems.append(s_Classes[x])

                s_MenuItems.append("Return")

                iClassChoice = int(GenFun.Menu(s_MenuItems))

                if iClassChoice == len(s_MenuItems) - 1:
                    
                    bLoop = False

                else: 

                    bLoop = False

                    o_StudentList[iMenuChoice - 1].sClassName = s_Classes[iClassChoice-1]

                    print("You have successfully assigned " + o_StudentList[iMenuChoice-1].GetName() + " to " + s_Classes[iClassChoice-1])

# ---------------------------Functions-----------------------------

LineBreak()

# ---------------------------Main Program-----------------------------

print("Welcome to the college registry menu\n")

# o_StudentList = [] # Create an empty list for the Student objects ----------------Replace next line of code with this one when testing is finished

o_StudentList = [Cls.Student("Joe", "Holmes", 25), Cls.Student("Jack", "Ryan", 33), Cls.Student("James", "Cameron", 44), Cls.Student("Jill", "Valentine", 30), Student("Lyse", "Hext", 26)]
# Test data above ^
s_Classes = ["Programming", "Maths", "English", "Pyhsics", "History"]


bContinue = True # Set up a variable for exiting a loop

while bContinue == True: # While bContinue is True, loop
  
    print("\n----------------College Registry Main Menu----------------\n")

    s_MenuItems = ["Please select an option:", "Register student", "Assign a student to a class", "Take a register", "Exit the program"]
# Creates a list of menu items to use, with the possibity of adding more
    sUserInput = GenFun.Menu(s_MenuItems) # Run the function Menu with the list of menu items, and assign the returned value to sUserInput

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