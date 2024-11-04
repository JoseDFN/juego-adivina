import random

print("Bienvenido al juuego de Adivinar el numero")

num_secreto = random.randint(1, 100)

intentos_maximos = 10
intentos_realizados = 0

while intentos_realizados < intentos_maximos:
    intento = int(input("Adivina el numero (entre 1 y 100): "))
    intentos_realizados += 1

    if intento == num_secreto:
        print(f"felicidades!, adivinaste el numero en {intentos_realizados} intentos")
        break
    elif intento < num_secreto:
        print(f"El numero secreto es mayor. \nTe quedan {intentos_maximos-intentos_realizados} intentos")
    else:
        print("El numero secreto es menor. \nTe quedan {intentos_maximos-intentos_realizados} intentos")

if intentos_realizados == intentos_maximos:
    print("Game over")