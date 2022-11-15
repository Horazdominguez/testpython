import random
matriz = []

for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(random.randint(0, 100))

print(matriz[0])
print(matriz[1])
print(matriz[2])
print(matriz[3])
print(matriz[4])

pos=0
e=0
f=0
if matriz[0][0] < matriz[0][1]:
    pos= pos +1
    if matriz[0][1] < matriz[0][2]:
        pos= pos +1
        if matriz[0][2] < matriz[0][3]:
            pos= pos +1
            print("Hay una secuencia que comienza en: ",e)
            print("Y finaliza en la posicion: ",pos)
            print("De la fila: ",f)
    
