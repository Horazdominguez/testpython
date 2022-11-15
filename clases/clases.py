class circulo():
	def __init__(self, radio):
		if radio < 0:
			print("Ingrese un valor real")
		else:
			self.radio = radio
		
		
	def area(self):
		try:
			area = 3.14 * (self.radio) ** 2
			print("El area es: ",area)
		except:
			None
			
	def perimetro(self):
		try:
			perimetro = 2*3.14*self.radio
			print("El Perimetro es: ",perimetro)
		except:
			None	

circulo1 = circulo(-13)
circulo1.area()
circulo1.perimetro()
