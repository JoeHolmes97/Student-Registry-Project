
# Module for generic functions that I may want to re-use

from Register_Classes import ValueOutOfRange


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
  
    return int(sUserInput) # Return the user input

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

def DisplayStudents(o_StudentList): # Function to diplay all students in the o_StudentList list
       
    for i in range(0, len(o_StudentList)): # Run through the student list

        print("\nName: " + o_StudentList[i].FirstName, o_StudentList[i].LastName) # Prints the first and last name of the student
        print("Age:", o_StudentList[i].Age) # Prints the students age

def DisplayStudentsBySubject(s_Subjects, subjectIndex):

    if len(s_Subjects[subjectIndex].classStudents) == 0:

        print("\n-----------" + s_Subjects[subjectIndex].className + "-----------\n\n")
        print("There are currently no Students assigned to this subject...\n")

    else:

        print("\n-----------" + s_Subjects[subjectIndex].className + "-----------\n\n")

        for x in range(0, len(s_Subjects[subjectIndex].classStudents)):

            print("\nName: " + s_Subjects[subjectIndex].classStudents[x].GetName())
            print("Age: " + str(s_Subjects[subjectIndex].classStudents[x].age))

def StudentSelectionMenu(o_StudentList, listMsg):

    s_MenuItems = [listMsg] # Create a list with this string as the only entry

    for i in range(0, len(o_StudentList)): # Loop a number of times equal to the number of students
        s_MenuItems.append(o_StudentList[i].FirstName + " " + o_StudentList[i].LastName) # Add the first and last name of the current student to the end of the list

    s_MenuItems.append("Return to main menu") # Add this option to the end of the list

    return Menu(s_MenuItems) # Run the Menu function with the list s_MenuItems