#Escribir un programa en Python que calcule la suma de números pares en una secuencia de números leídos del usuario, utilizando un ciclo for.

# Pedimos cuántos números se van a ingresar
cantidad = int(input("¿Cuántos números vas a ingresar?: "))

suma_pares = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    if numero % 2 == 0:
        suma_pares += numero

print(f"La suma de los números pares es: {suma_pares}")
