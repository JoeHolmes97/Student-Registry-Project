
# Module for inputting and outputting to files

from Register_Classes import Student

def SaveStudentDetails(myStudents, fileName):

	s = open(fileName + ".txt", "wt")

	for student in myStudents:

		s.write(student.firstName + "\n")
		s.write(student.lastName + "\n")
		s.write(str(student.age) + "\n")

	s.close()

def LoadStudentDetails(fileName):

	inputStudents = list()

	s = open(fileName + ".txt", "rt")

	for line in s:

		a = line
		b = s.readline()
		c = s.readline()

		inputStudents.append(Student(a, b, int(c)))

	return inputStudents

