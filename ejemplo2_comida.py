#In this example we use global and local variables
class species1:
	def __init__(self,name,init_energy):
		self.name = name
		self.energy = init_energy
	def eat(self,kg):
		global food
		if food >= kg:
			self.energy = self.energy + (kg*0.1)
			food = food - kg
	def refill(self,kg):
		global food
		food = food + kg



food = 20
indiv1 = species1("Lili",5)
indiv1.eat(5)
print (indiv1.name+" has "+str(indiv1.energy)+" of energy")
print ("Now there are "+str(food)+" of food")
indiv1.refill(10)
print ("Now there are "+str(food)+" of food")