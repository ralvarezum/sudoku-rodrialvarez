import math
import copy

class Sudoku():

    def __init__(self, list):
        self.board = list
        self.size = len(self.board)
        self.predefined_numbers = []
        self.transposed_table = []
        self.quadrants_list = []
        self.quadrant = int(math.sqrt(self.size))
        self.printed_board = ""

#Guardo las coordenadas (fila/columna) de los numeros pre-definidos.
        self.predefined_numbers = []
        for rows in range(self.size):
            for columns in range(len(self.board[rows])):
                if self.board[rows][columns] != "x":
                    self.predefined_numbers.append([rows, columns])

#Valido si alguno de los numeros se repite en las filas.
    def validate_rows(self, table):
        for row in table:
            for iteration in range(self.size):
                self.element = row.pop(iteration) #.pop quita el item en la posicion de la lista y lo devuelve.
                if self.element in row and self.element != "x":
                    return False
                row.insert(iteration, self.element)
        return True

#Valido el board. Valido si hay numeros repetidos en las columnas. Valido si hay algun numero repetido en los cuadrantes 3x3. 
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
        board_prt = ''
        for row in self.board:
            board_prt += ' | '.join(row)
            board_prt += '\n'      
        return board_prt
        
         
#Seteo el numero ingresado.
    def set_number(self, number, row, column):
            self.board_temp = copy.deepcopy(self.board)
            self.board[row][column] = str(number)
            if (not self.validate_board() or (row, column) in self.predefined_numbers):
                self.board = self.board_temp
                return "No puede ingresar un numero en esa coordenada!"
            return self.get_board()

#Valida si aun hay espacios libres en el board.
    def win(self):
        for iteration in range(self.size):
            if ("x" in self.board[iteration]):
                return False
        return True
        