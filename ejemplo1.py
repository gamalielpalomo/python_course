class Class1:
	def __init__(self):
		global energia
		energia = 5

	def correr(self):
		print ("corriendo...")
		if energia > 0:
			energia = energia - 1

	def comer(self,cant):
		print ("comiendo...")
		global energia
		energia = energia + (cant*0.2)

	def hablar(self):
		global energia
		print ("tengo "+str(energia)+" de energia")

class Class2:

	def __init__(self):
		self.energia = 5

	def correr(self):
		print ("Corriendo...")
		if energia > 0:
			energia = energia - 1

	def comer(self,cant):
		global energia
		print("Comiendo...")
		self.energia = self.energia + (cant*0.5)
		energia = energia + (cant*0.2)

	def hablar(self):
		print ("Tengo "+str(self.energia)+" de energia")


individuo1 =  Class1()
individuo1.comer(5)
individuo1.hablar()
individuo2 = Class2()
individuo2.comer(10)
individuo2.hablar()
print ("Energia global: "+str(energia))
energia = energia + 20
print ("Energia global: "+str(energia))
