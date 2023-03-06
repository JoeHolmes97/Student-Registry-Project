
# Module for registering classes

class ValueOutOfRange(Exception): # Creates a custom exception, which inherits from the exception class, called ValueOutOfRange
    pass # Do nothing

class Student: # Class for students

    sFirstName = "" # Create some member attributes to define the object
    sLastName = ""
    iAge = 0
    sSubjectName = ""
    bAttendance = False

    def __init__(self, sFirstName, sLastName, iAge): # Constructor used to initialise the student objects with data provided by the user

        self.FirstName = sFirstName
        self.LastName = sLastName
        self.Age = iAge
        # self.Class = sClassName
        #self.Attendance = bAttendance

    def PrintDetails(self): # Member function for printing the attributes of the object

        print(self.FirstName, self.LastName, self.iAge, self.bAttendance)

    def GetName(self): # Member function to return the students first and last name

        return self.FirstName + " " + self.LastName # Return the first and last name as a concatinated string

class Subjects():

    subjectName = ""
    subjectStudents = list()

    def __init__(self, subjectName):

        self.subjectName = subjectName
