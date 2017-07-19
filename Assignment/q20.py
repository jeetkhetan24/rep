"""
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

"""


class person:
	def __init(self):			# INIT BLOCK BECAUSE THE CLASS NEEDS TO CONTAIN ONE METHOD OR ELSE IT GIVES AND INTENDED BLOCK ERROR IN THE CHILD CLASS
		pass

class male(person):

	
	def getgender(self):
		print "MALE"

class female(person):
	
	def getgender(self):
		print "FEMALE"

male=male()
female=female()
male.getgender()
female.getgender()


