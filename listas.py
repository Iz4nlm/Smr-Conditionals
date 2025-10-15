

lista: list = [1, 2, 3, 4, 5, 6, 7] 

#print(lista[0:5]) #el 0:5 NO incluye el 5 se queda en el 4


indice: int = 1
contador_par: int = 0  
contador_inpar: int = 0

while indice <= 100:
    if indice % 2 == 0:
        contador_par += indice
        indice +=1
        print (contador_par)
    else:
        contador_inpar += indice
        indice += 1
        print(contador_inpar)

print (contador_inpar)
print (contador_par)