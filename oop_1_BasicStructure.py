class Dog:
	
	# A class attribute
	species = "mammal"

	# Initializer / Instance Attributes
	def __init__(self, name, age):
		self.name = name
		self.age = age

# Instantiate the Dog object
cairo = Dog("Cairo",3)
lili = Dog("Lili",5)

# Access the instance attributes
print("{0} is {1} and {2} is {3}.".format(cairo.name, cairo.age, lili.name, lili.age))

# Is Cairo a mammal?
if cairo.species == "mammal":
    print("{0} is a {1}!".format(cairo.name, cairo.species))