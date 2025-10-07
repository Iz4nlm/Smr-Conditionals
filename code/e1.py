# Creacion de variables

x: int = int(input("introduce X: "))
y: int = int(input("introduce Y: "))
mayor: int 
menor: int

if (x >=20 and x <30) and (y >=20 and x <30):
    if x > y:
        mayor = x
        menor = y
    else:
        mayor = y
        menor = x
    print(mayor)


# esto no hace falta, esta mejor la de arriba, es mas productivo
if (x < y):
    x = menor
else: 
    y = menor
