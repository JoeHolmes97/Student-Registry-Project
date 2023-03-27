
# Module for registering a students attendance

from Generic_Functions import (DisplayStudentsBySubject, StudentSelectionMenu)
from Assign_Students import SelectSubject

def TakeAttendance(s_Subjects):

	subjectChoice = SelectSubject(s_Subjects)

	if subjectChoice != len(s_Subjects) + 1:

		subjectChoice = subjectChoice - 1

		bLoop = True
		while bLoop == True:

			DisplayStudentsBySubject(s_Subjects, subjectChoice, False)

			studentSelection = StudentSelectionMenu(s_Subjects[subjectChoice].subjectStudents, "Select a student")

			if studentSelection != len(s_Subjects[subjectChoice].subjectStudents) + 1:

				if s_Subjects[subjectChoice].subjectStudents[studentSelection - 1].bAttendance == False:

					s_Subjects[subjectChoice].subjectStudents[studentSelection - 1].bAttendance = True

				else:

					s_Subjects[subjectChoice].subjectStudents[studentSelection - 1].bAttendance = False

			else:

				bLoop = False
