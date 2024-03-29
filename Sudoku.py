import math
import copy

class Sudoku():

    def __init__(self, list):
        list = [
                    ["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                    ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                    ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                    ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                    ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                    ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                    ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                    ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                    ["x", "x", "x", "x", "8", "x", "x", "7", "9"]]
        self.board = list
        self.size = 9
        self.predefined_numbers = []
        self.inverted_row_table = []
        self.quadrants_list = []
        self.column = []
        self.quadrant = int(math.sqrt(self.size))
        self.printed_board = ""

#Guardo las coordenadas (fila/columna) de los numeros pre-definidos.
        self.predefined_numbers = []
        for rows in range(self.size):
            for columns in range(len(self.board[rows])):
                if self.board[rows][columns] != "x":
                    self.predefined_numbers.append([rows, columns])

#Imprime el board.
    def get_board(self):
        board_prt = ''
        for row in self.board:
            board_prt += ' | '.join(row)
            board_prt += '\n'    
        return board_prt

#Valido si alguno de los numeros se repite en las filas.
    def validate_rows(self, table):
        for row in table:
            for iteration in range(self.size):
                self.item = row.pop(iteration)
                if self.item in row and self.item != "x":
                    return False
                row.insert(iteration, self.item)
        return True

#Valido el board. 
    def validate_board(self):
        if not self.validate_rows(self.board):
            return False
#Valido columnas
        for rows in range(self.size):
            self.column = []
            for columns in range(self.size):
                self.column.append(self.board[columns][rows])
            self.inverted_row_table.append(self.column)
        if not self.validate_rows(self.inverted_row_table):
            return False
#Valido quadrantes
        self.quadrants_list = []
        for rows in range(0, self.size, self.quadrant):
            for columns in range(0, self.size, self.quadrant):
                self.list_temporal = []
                for iteration in range(self.quadrant):
                    self.list_temporal.extend(self.board[rows+iteration][columns:columns+self.quadrant])
                self.quadrants_list.append(self.list_temporal)
        if not self.validate_rows(self.quadrants_list):
            return False
        return True        


#Seteo el numero ingresado.
    def set_number(self, number, row, column):
            self.board_temp = copy.deepcopy(self.board)
            self.board[row][column] = str(number)
            if ((row, column) in self.predefined_numbers or not self.validate_board()):
                self.board = self.board_temp
                return "No puede ingresar un numero en esa coordenada!"
            return self.get_board()

#Valida si aun hay espacios libres en el board.
    def end_game(self):
        count = 0
        for rows in range(self.size):
            for columns in range(self.size):
                if self.board[rows][columns] == "x":
                    count += 1
        if count < 1:
            return True
        else:
            return False
        