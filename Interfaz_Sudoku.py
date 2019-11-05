from api import api
from Sudoku import Sudoku
import time

class Interface ():

#Si el jugador lo desea, puede preguntar al iniciar la partida que es Sudoku.

    def help_sudoku(self):
        self.help = ""
        while self.help != "1" and self.help != "2":
            self.help = input("\nDeseas saber que es Sudoku? Ingrese 1(SI) o 2(NO)\n").lower()
            if self.help != "1" and self.help != "2":
                print("Solo 1 (SI) y 2 (NO) son las opciones disponibles! Vuelva a intentar!\n")
        if self.help == "1":
            print("\nLos Sudokus se suelen estructurar en cuadrículas divididas en cajas de 3x3 o 2x2 celdas en las que hay algunos números escritos de antemano. Para jugar, simplemente debes rellenar las celdas en blanco de tal forma que cada fila, columna y caja de 3x3 no tenga números repetidos.")
            time.sleep(3)
            print("\nGenerando Sudoku...")
            time.sleep(5)
            print("\nMuy bien! Que comience el juego!")
            print("\nSUDOKU GAME")
        elif self.help == "2":
            print("\nGenerando Sudoku...")
            time.sleep(5)
            print("\nMuy bien! Que comience el juego!")
            print("\nSUDOKU GAME") 


#Obtener tamaño del board.
    def get_size(self):
        self.size = 0
        while self.size != "4" and self.size != "9":
            self.size = input("\nIngrese el tamaño del tablero. Las opciones son 4 o 9: ")
            if self.size != "4" and self.size != "9":
                print("Ese tamaño no esta disponible. Las opciones son 4 o 9. Por favor, vuelva a intentar! \n\n")

#Inicializacion del juego.
    def start(self):
        self.help_sudoku()
        self.get_size()
        self.size = int(self.size)
        self.list = api(self.size)
        self.game = Sudoku(self.list)

#Check de los ingresos del user.
    def check_user_inputs(self, user_number, user_row, user_column):
        try:
            if int(user_row) > self.size or int(user_row) < 1:
                return False
            elif int(user_column) > self.size or int(user_column) < 1:
                return False
            elif user_number != "x":
                if int(user_number) > 0 and int(user_number) < self.size+1:
                    return True
            else:
                return True
        except Exception:
            return False

#Ingreso de numero, fila y columna. Si son invalidos, se le advierte al user.
    def user_inputs(self):
        self.u_number = input("Numero: ")
        self.u_row = input("Fila: ")
        self.u_column = input("Columna: ")
        print("\n")

        if self.check_user_inputs(self.u_number, self.u_row, self.u_column):
            return self.game.set_number(self.u_number, int(self.u_row)-1, int(self.u_column)-1)
        else:
            return "\nHa ingresado un numero,fila o columna invalido/a!"

#Jugando...hasta que gane el Sudoku.
    def play(self):
        self.start()
        print(self.game.get_board())
        while not self.game.win():
            print(self.user_inputs())
        print("\nYOU WIN!")


if __name__ == "__main__":
    juego = Interface()
    juego.play()