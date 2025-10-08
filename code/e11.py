print("Welcome to the menu")

n1: int = int(input("introduce el primer numero: "))
n2: int = int(input("introduce el segundo numero: "))
operacion: str = input("introduce el tipo de operacion que quieres realizar con los dos numeros")

if operacion == "+":
    print(n1 + n2)
elif operacion == "-":
    print(n1 - n2)
elif operacion == "*":
    print(n1 * n2)
else:
    print(n1 / n2)