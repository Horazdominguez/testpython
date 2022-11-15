import random
matriz = []

for i in range(5):						#Creamos una matriz de 5x5 
    matriz.append([])						#Con valores random de 0 a 100
    for j in range(5):
        matriz[i].append(random.randint(0, 100))

print(matriz[0])						#La mostramos
print(matriz[1])
print(matriz[2])
print(matriz[3])
print(matriz[4])

pos=0
e=0
f=0

for i in range(5):								#Recorremos las filas buscando numeros consecutivos ascendentes
	if matriz[i][0] < matriz[i][1]:
		pos= 0
		e=0
		f=0
		pos= pos +1
		if matriz[i][1] < matriz[i][2]:
			pos= pos +1
			if matriz[i][2] < matriz[i][3]:
				pos= pos +1
				print("Encontramos secuencias Horizontales")
				print("Hay una secuencia que comienza en: ",e+1)
				print("Y finaliza en la posicion: ",pos+1)
				print("De la fila: ",i+1)

for i in range(5):								#Recorremos las columnas buscando numeros consecutivos ascendentes
	if matriz[0][i] < matriz[1][i]:
		pos= 0
		e=0
		f=0
		pos= pos +1
		if matriz[1][i] < matriz[2][i]:
			pos= pos +1
			if matriz[2][i] < matriz[3][i]:
				pos= pos +1
				print("Encontramos secuencias Verticales")
				print("Hay una secuencia que comienza en: ",e+1)
				print("Y finaliza en la posicion: ",pos+1)
				print("De la columna: ",i+1)
    
