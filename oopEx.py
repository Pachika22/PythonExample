class Student:
	def __init__(self,sname,rollno,marks):
		self.sname = sname
		self.rollno =rollno
		self.marks = marks

	def talk(self):
		print('Name is:',self.sname)
		print('Roll No:',self.rollno)
		print('Marks are:',self.marks)

s = Student("Durga",101,90)
s.talk()