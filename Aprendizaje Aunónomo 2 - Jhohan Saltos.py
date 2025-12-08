import random

puntaje_jugador = 0
puntaje_computadora = 0
empates = 0

jugador = 0
computadora = 0

opciones = {
    1: "Piedra",
    2: "Papel",
    3: "Tijera"
}

while True:

    print("\nElige una opción:")
    print("1 = Piedra")
    print("2 = Papel")
    print("3 = Tijera")

    try:
        jugador = int(input("Tu elección: "))
    except:
        print("Debes ingresar un número. Intenta otra vez.")
        continue

    if jugador not in [1, 2, 3]:
        print("Opción inválida. Debes elegir entre 1, 2 o 3.")
        continue

    computadora = random.randint(1, 3)

    print(f"Jugador eligió: {opciones[jugador]}")
    print(f"Computadora eligió: {opciones[computadora]}")

    if jugador == computadora:
        print("Resultado: Empate")
        empates += 1

    elif (jugador == 1 and computadora == 3) or \
         (jugador == 2 and computadora == 1) or \
         (jugador == 3 and computadora == 2):

        print("Resultado: Gana el Jugador")
        puntaje_jugador += 1

    else:
        print("Resultado: Gana la Computadora")
        puntaje_computadora += 1

    print("\nPuntajes:")
    print(f"Jugador: {puntaje_jugador}")
    print(f"Computadora: {puntaje_computadora}")
    print(f"Empates: {empates}")

    while True:
        respuesta = input("\n¿Deseas jugar otra vez? (Si/No): ").strip().lower()

        if respuesta == "si":
            break

        elif respuesta == "no":
            print("¡Gracias por jugar!")
            exit()

        else:
            print("Respuesta no válida. Escribe exactamente: Si o No.")
