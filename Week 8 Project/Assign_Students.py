
# Module for assigning students

from Generic_Functions import (Menu,LineBreak,DisplayStudents,StudentSelectionMenu)

def SelectSubject():

    pass

def AssignStudents(o_StudentList, s_Subjects): # Function for assigning a student to a class

    bContinue = True

    while bContinue == True:

        DisplayStudents(o_StudentList) # Run the DisplayStudents function with the list o_StudentList

        print("\n----------------Assign Student----------------\n")

           # StudentSelectionMenu function goes here

        iMenuChoice = StudentSelectionMenu(o_StudentList, "Which student would you like to assign to a class?")

        if iMenuChoice == len(s_MenuItems) - 1: # If the user chooses the last menu option, do this
            
            bContinue = False # Set bContinue to False, exiting the loop

            LineBreak()

        else:

            bLoop = True

            while bLoop == True:
                
                s_MenuItems = ["\n Which class would you like to assign " + o_StudentList[iMenuChoice-1].GetName() + " to?"]

                for x in range(0, len(s_Subjects)):

                    s_MenuItems.append(s_Subjects[x].subjectName)

                s_MenuItems.append("Return")

                iSubjectChoice = int(Menu(s_MenuItems))

                if iSubjectChoice == len(s_MenuItems) - 1:
                    
                    bLoop = False

                else: 

                    bLoop = False

                    o_StudentList[iMenuChoice - 1].sSubjectName = s_Subjects[iSubjectChoice-1]

                    print("You have successfully assigned " + o_StudentList[iMenuChoice-1].GetName() + " to " + s_Subjects[iSubjectChoice-1].subjectName) # Error here, need to use name rather than object
