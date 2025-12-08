Algoritmo PiedraPapelTijera
	
    Definir Player, Pc Como Entero
    Definir continuar Como Cadena
	
    continuar <- "SI"
	
    Repetir
        Escribir "Elige una opción:"
        Escribir "1 = Piedra"
        Escribir "2 = Papel"
        Escribir "3 = Tijera"
        Leer Player
		
        Repetir
            Si (Player <> 1) Y (Player <> 2) Y (Player <> 3) Entonces
                Escribir "Opción inválida. Intenta nuevamente:"
                Leer Player
            FinSi
        Hasta Que (Player = 1) O (Player = 2) O (Player = 3)
		
        Pc <- Aleatorio(1,3)
		
        Escribir "Elección Player: ", Player
        Escribir "Elección PC es: ", Pc
		
        Si Player = Pc Entonces
            Escribir "Resultado: Empate."
        Sino
            Si (Player = 1 Y pc = 3) O (Player = 2 Y pc = 1) O (Player = 3 Y pc = 2) Entonces
                Escribir "Resultado: ¡Ganaste!"
            Sino
                Escribir "Resultado: Gana el PC."
            FinSi
        FinSi
		
        Repetir
            Escribir "¿Quieres jugar de nuevo? (SI/NO): "
            Leer continuar
        Hasta Que (continuar = "SI") O (continuar = "si") O (continuar = "NO") O (continuar = "no")
		
    Hasta Que (continuar = "NO") O (continuar = "no")
	
    Escribir "¡Gracias por jugar!"

FinAlgoritmo