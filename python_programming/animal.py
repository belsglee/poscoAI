class Animal:
	def __init__(self, name):
		self.name = name
	def speak(self):
		return "What the heck..?"

class Dog(Animal):
	def speak(self):
		return "멍!"

class Cat(Animal):
	def speak(self):
		return "야옹!"

class Cow(Animal):
	def speak(self):
		return "음메~~"

animallist = [Dog('Happy'), Dog('Walnut'), Cat('Ninja'), Cow("MooMoo")]

for a in animallist:
	print(a.name + ": " + a.speak())
