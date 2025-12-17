Proceso PiedraPapelTijera
    Definir jugador, computadora, pJugador, pComputadora, empates Como Entero
    Definir resultado, resp Como Cadena
	
    pJugador <- 0
    pComputadora <- 0
    empates <- 0
	
    Repetir
        Escribir "-----------------------"
        Escribir "Elige una opción:"
        
        Escribir "1. Piedra"
        Escribir "2. Papel"
        Escribir "3. Tijera"
        Escribir "-----------------------"
        
        Leer jugador
		
        Mientras jugador < 1 O jugador > 3 Hacer
            Escribir "Opcion incorrecta. Intente de nuevo:"
            Leer jugador
        FinMientras
		
        computadora <- Aleatorio(1,3)
		
        Escribir "Tu elegiste: ", jugador
        Escribir "PC eligio: ", computadora
		
        Si jugador = computadora Entonces
            resultado <- "empate"
        Sino
            Si (jugador=1 Y computadora=3) O (jugador=2 Y computadora=1) O (jugador=3 Y computadora=2) Entonces
                resultado <- "ganaste"
            Sino
                resultado <- "perdiste"
            FinSi
        FinSi
		
        Si resultado = "empate" Entonces
            Escribir ">> Fue un Empate <<"
            empates <- empates + 1
        Sino
            Si resultado = "ganaste" Entonces
                Escribir ">> Ganaste esta ronda <<"
                pJugador <- pJugador + 1
            Sino
                Escribir ">> Gano la PC <<"
                pComputadora <- pComputadora + 1
            FinSi
        FinSi
		
        Escribir "Puntos TU: ", pJugador
        Escribir "Puntos PC: ", pComputadora
        Escribir "Empates: ", empates
		
        Escribir "¿Jugar otra vez? (si/no)"
        Leer resp
    Hasta Que resp = "no" O resp = "NO"
	
    Escribir "Fin del juego"
FinProceso