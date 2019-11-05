from api import api
from Sudoku import Sudoku

class Interface ():
    
#Inicializacion del juego.
    def start(self):
        self.size = 9
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
        print("\nSUDOKU GAME\n")
        print(self.game.get_board())
        while not self.game.win():
            print(self.user_inputs())
        print("\nYOU WIN!")


if __name__ == "__main__":
    juego = Interface()
    juego.play()