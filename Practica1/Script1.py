import random

class Marcador:
    def __init__(self, numSet, juego, puntos):
        self.numSet = numSet
        self.juego = juego
        self.puntos = puntos


class Jugador:
    def __init__(self, nombre, marcador):
        self.nombre = nombre
        self.marcador = marcador

class Juego:
    def __init__(self, ganador, jugadorJ1, jugadorJ2, setsAJugar, servidor):
        self.ganador = ganador
        self.jugadorJ1 = jugadorJ1
        self.jugadorJ2 = jugadorJ2
        self.setsAJugar = setsAJugar
        self.servidor = servidor

    def cambiaSaque(self):
        if self.servidor == 1:
            self.servidor = 2
        else:
            self.servidor = 1

    def sumaPunto(self, numeroJugador):
        if numeroJugador == 1:
            if self.jugadorJ2.marcador.puntos == 40 and self.jugadorJ1.marcador.puntos == 40:
                self.jugadorJ1.marcador.puntos = 'adv'
            elif self.jugadorJ1.marcador.puntos == 40 and self.jugadorJ2.marcador.puntos == 'adv':
                self.jugadorJ2.marcador.puntos = 40
            elif self.jugadorJ1.marcador.puntos == 40 or self.jugadorJ1.marcador.puntos == 'adv':
                self.jugadorJ1.marcador.puntos = 0
                self.jugadorJ2.marcador.puntos = 0
                self.cambiaSaque()
                self.sumaJuego(1)
                if ((self.jugadorJ1.marcador.juego + self.jugadorJ2.marcador.juego) % 2 == 0) and (self.jugadorJ1.marcador.juego + self.jugadorJ2.marcador.juego) != 0:
                    print("__________Cambio de cancha__________")
            elif self.jugadorJ2.marcador.puntos == 'adv':
                self.jugadorJ2.marcador.puntos = 40
            elif self.jugadorJ1.marcador.puntos == 0:
                self.jugadorJ1.marcador.puntos = 15
            elif self.jugadorJ1.marcador.puntos == 15:
                self.jugadorJ1.marcador.puntos = 30
            elif self.jugadorJ1.marcador.puntos == 30:
                self.jugadorJ1.marcador.puntos = 40
        elif numeroJugador == 2:
            if self.jugadorJ1.marcador.puntos == 40 and self.jugadorJ2.marcador.puntos == 40:
                self.jugadorJ2.marcador.puntos = 'adv'
            elif self.jugadorJ2.marcador.puntos == 40 and self.jugadorJ1.marcador.puntos == 'adv':
                self.jugadorJ1.marcador.puntos = 40
            elif self.jugadorJ2.marcador.puntos == 40 or self.jugadorJ2.marcador.puntos == 'adv':
                self.jugadorJ2.marcador.puntos = 0
                self.jugadorJ1.marcador.puntos = 0
                self.cambiaSaque()
                self.sumaJuego(2)
                if ((self.jugadorJ1.marcador.juego + self.jugadorJ2.marcador.juego) % 2 == 0) and (self.jugadorJ1.marcador.juego + self.jugadorJ2.marcador.juego) != 0:
                    print("__________Cambio de cancha__________")
            elif self.jugadorJ1.marcador.puntos == 'adv':
                self.jugadorJ1.marcador.puntos = 40
            elif self.jugadorJ2.marcador.puntos == 0:
                self.jugadorJ2.marcador.puntos = 15
            elif self.jugadorJ2.marcador.puntos == 15:
                self.jugadorJ2.marcador.puntos = 30
            elif self.jugadorJ2.marcador.puntos == 30:
                self.jugadorJ2.marcador.puntos = 40

    def sumaJuego(self, numeroJugador):
        if numeroJugador == 1:
            self.jugadorJ1.marcador.juego += 1
            if self.jugadorJ1.marcador.juego >= 6:
                if abs(self.jugadorJ2.marcador.juego - self.jugadorJ1.marcador.juego) >= 2:
                    self.jugadorJ1.marcador.juego = 0
                    self.jugadorJ2.marcador.juego = 0
                    self.sumaSet(1)
        elif numeroJugador == 2:
            self.jugadorJ2.marcador.juego += 1
            if self.jugadorJ2.marcador.juego >= 6:
                if abs(self.jugadorJ2.marcador.juego - self.jugadorJ1.marcador.juego) >= 2:
                    self.jugadorJ2.marcador.juego = 0
                    self.jugadorJ1.marcador.juego = 0
                    self.sumaSet(2)

    def sumaSet(self, numeroJugador):
        if numeroJugador == 1:
            self.jugadorJ1.marcador.numSet += 1
            if (self.setsAJugar//2 + 1) <= self.jugadorJ1.marcador.numSet:
                self.ganador = 1
        else:
            self.jugadorJ2.marcador.numSet += 1
            if (self.setsAJugar//2 + 1) <= self.jugadorJ2.marcador.numSet:
                self.ganador = 2

if __name__ == "__main__":

    marcadorJugador1 = Marcador(0, 0, 0)
    marcadorJugador2 = Marcador(0, 0, 0)

    while True:
        nombreJugador1 = input("Ingrese el nombre del Jugador 1: ")
        if nombreJugador1.isalpha():
            break
        else:
            print("Por favor, ingrese un nombre válido que contenga solo letras.")

    while True:
        nombreJugador2 = input("Ingrese el nombre del Jugador 2: ")
        if nombreJugador2.isalpha():
            break
        else:
            print("Por favor, ingrese un nombre válido.")

    jugador1 = Jugador(nombreJugador1, marcadorJugador1)
    jugador2 = Jugador(nombreJugador2, marcadorJugador2)

    while True:
        try:
            setsAJugarMain = input("Ingrese el número de sets a jugar: ")
            lista_caracteres = list(setsAJugarMain)
            for caracter in lista_caracteres:
                if not caracter.isdigit():
                    raise ValueError("Solo se aceptan numeros")
                else:
                    setsAJugarMain = int(setsAJugarMain)
            if setsAJugarMain % 2 == 0 or setsAJugarMain < 3:
                raise ValueError("El número de sets debe ser impar y al menos 3")
            juego = Juego(None, jugador1, jugador2, setsAJugarMain, random.randint(1, 2))
            break
        except ValueError as e:
            print(e)
            print("Por favor, ingrese un número de sets válido.")

    print("Saca el jugador: ", juego.servidor)

    # Empieza el juego
    while juego.ganador is None:

        print('=======================================================================================')

        # Solicitar al usuario que ingrese quién anota
        while True:
            try:
                jugadorQueAnota = input(f"Ingrese el número del jugador que anota (1: {jugador1.nombre}, 2: {jugador2.nombre}): ")
                lista_caracteres2 = list(jugadorQueAnota)
                for caracter2 in lista_caracteres2:
                    if not caracter2.isdigit():
                        raise ValueError("Solo se aceptan numeros")
                    else:
                        jugadorQueAnota = int(jugadorQueAnota)
                if jugadorQueAnota not in [1, 2]:
                    raise ValueError("Número de jugador inválido")
                break
            except ValueError as e:
                print(e)
                print("Por favor, ingrese un número de jugador válido.")

        # Registrar el punto para el jugador que anota
        juego.sumaPunto(jugadorQueAnota)

        # Imprime el jugador que Saca
        print("Saca el jugador: ", juego.servidor)

        # Imprimir el marcador de ambos jugadores
        print("Marcador del jugador 1:", jugador1.marcador.numSet, jugador1.marcador.juego, jugador1.marcador.puntos)
        print("Marcador del jugador 2:", jugador2.marcador.numSet, jugador2.marcador.juego, jugador2.marcador.puntos)

    # Imprimir el ganador del juego
    if juego.ganador == 1:
        print("El ganador del juego es", jugador1.nombre)
    else:
        print("El ganador del juego es", jugador2.nombre)
