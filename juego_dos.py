import random


def juego_dos():
    # FFF
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    # GGFG

    print("Bienbenido al juego de adivinanzas de numero")
    print("Debes adivinar un numero del 1 al 100")
    print("Intenta adivinar!")

    while not adivinado:
        adivinanza = input("Introduzca un numero del 1 al 100 ")
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"Numero secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El numero secreto es menor a {adivinanza}")
            else:
                print(f"Felicitaciones has acertado el numero en {intentos} intentos. ")
        else:
            print("Ingresa un numero por favor")


juego_dos()
