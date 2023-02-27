
# Week 8 Project - College registry system
#  - Dynamic menu - menu inside function
#  - Register student, assign student to class, take register, exit program
# - Inside list

# ---------------------------Classes-----------------------------

class MenuOutOfRange(Exception): # Creates a custom class, which inherits from the exception class, called MenuOutOfRange
  pass # Do nothing

class Student: # Create a class called student
  sFirstName = "" # Create some variables inside the class
  sLastName = ""
  iUserAge = 0
  sUserName = ""
  bAttendance = False

  def __init__(self, sFirstName, sLastName, sUserName): # Initialise the variables with data provided by the user
    self.FirstName = sFirstName
    self.LastName = sLastName
    self.Username = sUserName

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
      raise MenuOutOfRange # Raise the custom exception

  except MenuOutOfRange: # If the custom exception MenuOutOfRange is raised, do this
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

# ---------------------------Functions-----------------------------

LineBreak()

# ---------------------------Main Program-----------------------------

print("Welcome to the college registry menu\n")

bContinue = True # Set up a variable for exiting a loop

while bContinue == True: # While bContinue is True, loop
  
  s_MenuItems = ["Please select an option:", "Register student", "Assign a student to a class", "Take a register", "Exit the program"]
# Creates a list of menu items to use, with the possibity of adding more
  sUserInput = Menu(s_MenuItems) # Run the function Menu with the list of menu items, and assign the returned value to sUserInput

  LineBreak()

  if sUserInput == "1": # If the user enters 1, do this
    
    o_StudentList = [] # Create an empty list for the Student objects

    bLoop = True # Create a variable for exiting a loop

    while bLoop == True: # While bLoop is True, do this
    
      sFirstName = input("Please enter the students first name: ") # Asks the user for a first name
      sLastName = input("Please enter the students last name: ") # Asks the user for a last name
      sUserName = input("Please enter a username for the student or leave blank to use a pre-generated username (for example: JSmith): ")
      if sFirstName == "" or sLastName == "": # If the first name or last name variables are left empty, do this
        print("\nYou need to enter both a first name and a last name")
        
      else: # If the first if-statement doesn't trigger, do this

        if sUserName == "":
          sUserName = sFirstName[:1] + sLastName[:]
          print(sUserName)
        
        bLoop = False # Set bLoop to False, exiting the loop
        
    o_StudentList.append(Student(sFirstName, sLastName, sUserName)) # Create an object with the properties of sFirstName and sLastName and append it to the end of the list
    print(o_StudentList[-1].FirstName, o_StudentList[-1].LastName, o_StudentList[-1].Username) # Print the students first and last name for the object just created

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