
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


                   


# ---------------------------Functions-----------------------------

LineBreak()

# ---------------------------Main Program-----------------------------

def MainProgram():

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
        
            GenFun.DisplayStudents(o_StudentList)

            LineBreak()
  
        elif sUserInput == "2": # Assign a student to a class, not coded yet
       
            AssignStudents(o_StudentList, s_Classes)

        elif sUserInput == "3":
            print("Coming soon 3") # Take a register, not coded yet

        elif sUserInput == "4": # Option for exiting the program
            print("Exiting the program")
            bContinue = False # Set bContinue to false, exiting the program

Main() # Runs the main program function

# ---------------------------Main Program-----------------------------


# To search through the list of objects for a specific person, use for loop to loop through list, comparing the values to the user input
# Use function inside the 'Class' class to add students to a list i.e add students to Class register