direccion: str = input("Introduce una direccion: ")
direccion_contraria: str 


if direccion != "arriba" and direccion != "abajo" and direccion != "izquierda" and direccion != "derecha":
    print("no son iguales")
else:
    if direccion == "arriba":
        direccion_contraria = "abajo"
    elif direccion == "abajo":
        direccion_contraria = "arriba"
    elif direccion == "izquierda":
        direccion_contraria = "derecha"
    else:
        direccion_contraria = "izquierda"
print(direccion_contraria)
print("se acaboo")