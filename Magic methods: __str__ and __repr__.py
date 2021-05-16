#str methods -->  turn your object into a string.
#repr methods --> used to print out an unambiguous representation of an object.so that you can use that to recreate the object. debug propose.


class Person:
   def __init__(self, name, age):
     self.name = name
     self.age = age
	 
   def __str__(self):
     return f"Person {self.name}, {self.age} years old"

   def __repr__(self):
     return f"<person('{self.name}', {self.age})>"
		

bob = Person("Bob", 35)
print(bob)
