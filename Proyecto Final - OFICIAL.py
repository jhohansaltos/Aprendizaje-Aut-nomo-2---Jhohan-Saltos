import random

OPCIONES_VALIDAS = (1, 2, 3)
RESPUESTAS_VALIDAS = ("si", "no")

opciones = {
    1: "Piedra",
    2: "Papel",
    3: "Tijera"
}

reglas = {
    (1, 3): "Jugador",
    (2, 1): "Jugador",
    (3, 2): "Jugador"
}

puntajes = {
    "jugador": 0,
    "computadora": 0,
    "empates": 0
}

def obtener_eleccion_jugador():
    """Pide la elección del jugador y la valida"""
    try:
        eleccion = int(input("Tu elección: "))
        if eleccion in OPCIONES_VALIDAS:
            return eleccion
        else:
            print("Opción inválida. Elige 1, 2 o 3.")
            return None
    except:
        print("Debes ingresar un número.")
        return None

def obtener_eleccion_computadora():
    """Genera una elección aleatoria para la computadora"""
    return random.choice(OPCIONES_VALIDAS)

def determinar_ganador(jugador, computadora):
    """Determina quién gana la ronda"""
    if jugador == computadora:
        return "empate"
    elif (jugador, computadora) in reglas:
        return "jugador"
    else:
        return "computadora"

def mostrar_puntajes():
    print("\nPuntajes:")
    print(f"Jugador: {puntajes['jugador']}")
    print(f"Computadora: {puntajes['computadora']}")
    print(f"Empates: {puntajes['empates']}")

while True:
    print("\nElige una opción:")
    for clave, valor in opciones.items():
        print(f"{clave} = {valor}")

    jugador = None
    while jugador is None:
        jugador = obtener_eleccion_jugador()

    computadora = obtener_eleccion_computadora()

    print(f"\nJugador eligió: {opciones[jugador]}")
    print(f"Computadora eligió: {opciones[computadora]}")

    resultado = determinar_ganador(jugador, computadora)

    if resultado == "empate":
        print("Resultado: Empate")
        puntajes["empates"] += 1
    elif resultado == "jugador":
        print("Resultado: Gana el Jugador")
        puntajes["jugador"] += 1
    else:
        print("Resultado: Gana la Computadora")
        puntajes["computadora"] += 1

    mostrar_puntajes()

    respuesta = input("\n¿Deseas jugar otra vez? (Si/No): ").strip().lower()
    if respuesta not in RESPUESTAS_VALIDAS or respuesta == "no":
        print("¡Gracias por jugar!")
        break