# Simple class objects
class Student:
	ucsc_student = True                      # Defined by default

	def __init__(self, user_name, user_age): # The constructor. Must be named __init__, and must have self as an argument
		self.name = user_name
		self.age = user_age

	
	def birthday(self):                      # Simple class function that increments a student's age by one
		self.age += 1                        # Any time we want to access a class object's variables, we must include self in the arguments

jon_chong = Student('Jon Chong', 21)
print(jon_chong.name, jon_chong.age)

jon_chong.birthday()
print(jon_chong.age)
