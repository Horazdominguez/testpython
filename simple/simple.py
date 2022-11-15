import random

def simple():
    lst =[{'id':0, 'edad':'0'} for i in range(10)]  #Genero una lista de Diccionarios
    for i in range(10):                             #Le doy un id de 0 a 9
        lst[i]['id'] = i
    for i in range(10):                             #Les asigno una edad aleatoria de 18 a 100
        lst[i]['edad'] = random.randint(18, 100)
    return lst                                      #Devuelvo la Lista



def rsimple(e):
    mayor_edad=sorted(e, key=lambda x: x["edad"])[-1] 
    print("La persona de mayor edad es la que posee el ID: ", mayor_edad) #Imprimo en pantalla el Id de la persona de mayor edad
    menor_edad=sorted(e, key=lambda x: x["edad"])[1]                      #Imprimo en pantalla el Id de la persona de menor edad
    print("La persona de menor edad es la que posee el ID: ", menor_edad)                                     
    for i in range(10):                             #Muestro la lista ordenada por id de mayor a menor
        print(e[9-i])


rsimple(simple())



