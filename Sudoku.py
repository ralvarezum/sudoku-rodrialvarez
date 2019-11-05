import math
import copy

class Sudoku():

    def __init__(self, list):
        self.board = list
        self.size = len(self.board)
        self.quadrant = int(math.sqrt(self.size))
        self.predefined_numbers = []
        self.transposed_table = []
        self.quadrants_list = []
        self.printed_board = ""

#Guardo las coordenadas (fila/columna) de los numeros pre-definidos.
        self.predefined_numbers = []
        for rows in range(self.size):
            for columns in range(len(self.board[rows])):
                if (self.board[rows][columns] != "x"):
                    self.predefined_numbers.append((rows, columns))

#Valido si alguno de los numeros se repite en las filas.
    def validate_rows(self, table):
        for row in table:
            for iteration in range(self.size):
                self.element = row.pop(iteration)
                if self.element in row and self.element != "x":
                    return False
                row.insert(iteration, self.element)
        return True

#Valido el board. Valido si hay numeros repetidos en las columnas. Valido si hay algun numero repetido en los cuadrantes. 
    def validate_board(self):
        if not self.validate_rows(self.board):
            return False

        self.transposed_table = []
        for rows in range(self.size):
            self.column = []
            for columns in range(self.size):
                self.column.append(self.board[columns][rows])
            self.transposed_table.append(self.column)

        if not self.validate_rows(self.transposed_table):
            return False

        self.quadrants_list = []
        for rows in range(0, self.size, self.quadrant):
            for columns in range(0, self.size, self.quadrant):
                self.zed_list = []
                for iteration in range(self.quadrant):
                    self.zed_list.extend(self.board[rows+iteration][columns:columns+self.quadrant])
                self.quadrants_list.append(self.zed_list)

        if not self.validate_rows(self.quadrants_list):
            return False
        return True

#Imprime el board.
    def get_board(self):
        self.printed_board = ""
        for rows in range(self.size):
            if rows == self.quadrant or rows == self.quadrant*2:
                for iteration in range(self.size):
                    self.printed_board += "--"
                    if iteration == self.quadrant-1 or iteration == self.quadrant*2-1:
                        self.printed_board += "++-"
                if iteration == self.quadrant-1 or iteration == self.quadrant*2-1:
                    self.printed_board = self.printed_board[:-3]
                self.printed_board += "\n"
            for columns in range(self.size):
                if columns == self.quadrant or columns == self.quadrant*2:
                    self.printed_board += "|| "
                self.printed_board += self.board[rows][columns] + " "
            self.printed_board += "\n"
        return self.printed_board

#Seteo el numero ingresado. Se crea un duplicado del board original en caso de que el numero ingresado no cumpla con las condiciones. Si no se cumple, el board duplicado se iguala al board original.
    def set_number(self, number, row, column):
        self.board_temp = copy.deepcopy(self.board)
        self.board[row][column] = str(number)
        if (not self.validate_board() or (row, column) in self.predefined_numbers):
            self.board = self.board_temp
            return "No puede ingresar un numero en esa coordenada!"
        return self.get_board()

#Valida si aun hay 'x' en el tablero.
    def win(self):
        for iteration in range(self.size):
            if ("x" in self.board[iteration]):
                return False
        return True