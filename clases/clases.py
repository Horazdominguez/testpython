class circulo():
	def __init__(self, radio):				#Defino la clase circulo
		if radio < 0:
			print("Ingrese un valor real")
		else:
			self.radio = radio
		
		
	def area(self):						#Agrego el metodo Area
		try:
			area = 3.14 * (self.radio) ** 2		#Uso try para las excepciones que me puede dar 
			print("El area es: ",area)		
		except:
			None
			
	def perimetro(self):					#Agrego el metodo perimetro
		try:
			perimetro = 2*3.14*self.radio
			print("El Perimetro es: ",perimetro)
		except:
			None	
			
	def __str__(self):					#Agrego __str__ para que me devuelva un intento de dibujo cuando lo imprimo
		try:
			if self.radio > 0:
				print("--------")
				print("|      |")
				print("|      |")
				print( " _______")
				print("Parece un circulo")
				return "Use la imaginaciòn"
			else:
				return ""			 #Agrego esta linea para que no me de error cuando ingresas radio = 0
		except:
			return "No hay circulo"
			
			
R = int(input("Ingrese el Radio del circulo: "))		#Pedimos el ingreso del Radio
circulo1 = circulo(R)						#Creamos el objeto circulo1 del tipo circulo
circulo1.area()							#Llamamos al metodo area
circulo1.perimetro()						#Lamamos al metodo perimetro
print()
print()
print(circulo1)							#Imprimimos la representacion del circulo que nos devuelve str


