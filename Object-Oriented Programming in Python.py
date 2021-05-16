class Student:
  def __init__(self):
    self.name = "Rolf"
    self.grades = (90,96,87,86)
		
  def average_grade(self):
	  return sum(self.grades) / len(self.grades)
		 
student = Student()
print(student.average_grade())


class Student1:
  def __init__(self,name,grade):
    self.name = name
    self.grades = grade
		
  def average_grade(self):
	  return sum(self.grades) / len(self.grades)


student = Student1("raj", (1,2,3,4))
print(student.average_grade())
