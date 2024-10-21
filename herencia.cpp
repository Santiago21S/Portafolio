import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al juego de Adivina el Número!")
    print("He elegido un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:
        try:
            adivinanza = int(input("Introduce tu adivinanza: "))
            intentos += 1

            if adivinanza < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

adivina_el_numero()
