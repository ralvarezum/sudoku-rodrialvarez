import unittest
import io
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from Interfaz_Sudoku import Interface
from Sudoku import Sudoku


"""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////"""
"""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////"""
"""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////"""
"""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////"""


class TestInterfaceSudoku(unittest.TestCase):
    def setUp(self):

        self.user_9 = Interface()
        list_nine_9 = [
                    ["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                    ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                    ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                    ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                    ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                    ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                    ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                    ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                    ["x", "x", "x", "x", "8", "x", "x", "7", "9"]]

        self.user_9.size = 9
        self.user_9.level = "1"
        self.user_9.game = Sudoku(list_nine_9)

    @parameterized.expand([
        ("y", "4", "6"),
        ("2", "k", "6"),
        ("2", "4", "d"),
        ("@", "4", "6"),
        ("2", "@", "6"),
        ("2", "4", "@"),
        ("!", "4", "@"),
        ("+", "g", "6"),
        ("3", "asd", "+"),
        ("+", "-", "d"),
        ("hola", "asd", "@"),
        ("+", "asd", "hola")
    ])

    def test_put_simbols(self, number, row, column):
        result = self.user_9.check_user_inputs(number, row, column)
        self.assertFalse(result)

    @parameterized.expand([
        ("2", "0", "1"),
        ("2", "-1", "1"),
        ("2", "10", "1"),
        ("2", "100", "1")
    ])
    def test_put_wrong_rows(self, number, row, column):
        mock = MagicMock()
        mock.side_effect = [number, row, column]
        with patch("builtins.input", new=mock):
            result = self.user_9.user_inputs()
        self.assertEqual(result, "\nHa ingresado un numero,fila o columna invalido/a!")

    @parameterized.expand([
        ("2", "1", "0"),
        ("2", "1", "-1"),
        ("2", "1", "10"),
        ("2", "1", "100")
    ])
    def test_put_wrong_columns(self, number, row, column):
        mock = MagicMock()
        mock.side_effect = [number, row, column]
        with patch("builtins.input", new=mock):
            result = self.user_9.user_inputs()
        self.assertEqual(result, "\nHa ingresado un numero,fila o columna invalido/a!")

    @parameterized.expand([
        ("0", "2", "1"),
        ("-1", "2", "1"),
        ("10", "2", "1"),
        ("100", "2", "1")
    ])
    def test_put_wrong_numbers(self, number, row, column):
        mock = MagicMock()
        mock.side_effect = [number, row, column]
        with patch("builtins.input", new=mock):
            result = self.user_9.user_inputs()
        self.assertEqual(result, "\nHa ingresado un numero,fila o columna invalido/a!")

    @parameterized.expand([
        ("2", "2", "2"),
        ("7", "2", "2"),
        ("1", "2", "1"),
        ("4", "1", "3")

    ])
    def test_put_correct_numbers(self, number, row, column):
        mock = MagicMock()
        mock.side_effect = [number, row, column]
        with patch("builtins.input", new=mock):
            result = self.user_9.user_inputs()
        self.assertNotEqual(result, "\nHa ingresado un numero,fila o columna invalido/a!")


    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_winning_nine_9(self, mock_stdout):

        mock = MagicMock()
        mock.side_effect = ["4", "1", "3",
                            "6", "1", "4",
                            "8", "1", "6",
                            "9", "1", "7",
                            "1", "1", "8",
                            "2", "1", "9",
                            "7", "2", "2",
                            "2", "2", "3",
                            "1", "2", "4",
                            "3", "2", "7",
                            "4", "2", "8",
                            "8", "2", "9",
                            "1", "3", "1",
                            "3", "3", "4",
                            "4", "3", "5",
                            "2", "3", "6",
                            "5", "3", "7",
                            "7", "3", "9",
                            "5", "4", "2",
                            "9", "4", "3",
                            "7", "4", "4",
                            "1", "4", "6",
                            "4", "4", "7",
                            "2", "4", "8",
                            "2", "5", "2",
                            "6", "5", "3",
                            "5", "5", "5",
                            "7", "5", "7",
                            "9", "5", "8",
                            "1", "6", "2",
                            "8", "8", "2",
                            "7", "8", "3",
                            "6", "8", "7",
                            "3", "8", "8",
                            "3", "9", "1",
                            "4", "9", "2",
                            "5", "9", "3",
                            "2", "9", "4",
                            "6", "9", "6",
                            "3", "6", "3",
                            "9", "6", "4",
                            "4", "6", "6",
                            "8", "6", "7",
                            "5", "6", "8",
                            "9", "7", "1",
                            "1", "7", "3",
                            "5", "7", "4",
                            "3", "7", "5",
                            "7", "7", "6",
                            "4", "7", "9",
                            "2", "8", "1",
                            "1", "9", "7"]
        with patch("Interfaz_Sudoku.Interface.start",
                   return_value=None), patch("builtins.input", new=mock):
            self.user_9.play()
        self.assertEqual(mock_stdout.getvalue()[-11:], "\n\nYOU WIN!\n")

"""//////////SUDOKU////////""""""//////////SUDOKU////////""""""//////////SUDOKU////////""""""//////////SUDOKU////////"""
"""//////////SUDOKU////////""""""//////////SUDOKU////////""""""//////////SUDOKU////////""""""//////////SUDOKU////////"""
"""//////////SUDOKU////////""""""//////////SUDOKU////////""""""//////////SUDOKU////////""""""//////////SUDOKU////////"""
"""//////////SUDOKU////////""""""//////////SUDOKU////////""""""//////////SUDOKU////////""""""//////////SUDOKU////////"""


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.sudoku_9 = Sudoku([
            ["5", "3", "x", "x", "7", "x", "x", "x", "x"],
            ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
            ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
            ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
            ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
            ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
            ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
            ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
            ["x", "x", "x", "x", "8", "x", "x", "7", "9"]
                               ])
    def test_nice_board_nine_9(self):
        self.assertTrue(self.sudoku_9.validate_board())

    @parameterized.expand([
        (7, 0, 2),
        (5, 1, 7),
        (6, 2, 3),
        (8, 3, 6),
        (4, 4, 4),
        (7, 5, 6),
        (6, 6, 3),
        (9, 7, 0),
        (8, 8, 1),
        (5, 8, 0),
        (3, 8, 1),
        (8, 7, 2),
        (4, 0, 3),
        (7, 6, 4),
        (9, 0, 5),
        (2, 0, 6),
        (6, 7, 7),
        (9, 0, 8),
        (3, 2, 0),
        (9, 0, 3),
        (6, 0, 8),
        (7, 3, 2),
        (2, 3, 5),
        (6, 3, 6),
        (6, 8, 0),
        (9, 8, 3),
        (8, 8, 6)
    ])
    def test_wrong_numbers_nine_9(self, number, row, column):
        result = self.sudoku_9.set_number(number, row, column)
        self.assertEqual(result,"No puede ingresar un numero en esa coordenada!")

    @parameterized.expand([
        (6, 4, 2),
        (5, 4, 4),
        (7, 4, 6),
        (9, 4, 7),
        (1, 5, 1),
        (4, 0, 2),
        (6, 0, 3),
        (8, 0, 5),
        (9, 0, 6),
        (1, 0, 7),
        (2, 0, 8),
        (7, 1, 1),
        (2, 1, 2),
        (1, 1, 3),
        (3, 1, 6),
        (4, 1, 7),
        (8, 1, 8),
        (1, 2, 0),
        (3, 2, 3),
        (5, 5, 7),
        (9, 6, 0),
        (1, 6, 2),
        (5, 6, 3),
        (3, 6, 4),
        (7, 6, 5),
        (4, 6, 8),
        (2, 7, 0),
        (8, 7, 1),
        (7, 7, 2),
        (6, 7, 6),
        (3, 7, 7),
        (4, 2, 4),
        (2, 2, 5),
        (5, 2, 6),
        (7, 2, 8),
        (5, 3, 1),
        (9, 3, 2),
        (7, 3, 3),
        (1, 3, 5),
        (4, 3, 6),
        (2, 3, 7),
        (2, 4, 1),
        (3, 5, 2),
        (9, 5, 3),
        (4, 5, 5),
        (8, 5, 6),
        (3, 8, 0),
        (4, 8, 1),
        (5, 8, 2),
        (2, 8, 3),
        (6, 8, 5),
        (1, 8, 6),
    ])
    def test_nice_numbers_nine_9(self, number, row, column):
        result = self.sudoku_9.set_number(number, row, column)
        self.assertNotEqual(result,"No puede ingresar un numero en esa coordenada!")

    @parameterized.expand([
        ("7", 5, 6),
        ("6", 6, 3),
        ("9", 7, 0),
        ("7", 0, 2),
        ("5", 1, 7),
        ("6", 2, 3),
        ("8", 3, 6),
        ("4", 4, 4),
        ("8", 8, 1),
        ])
    def test_valid_rows_nine_9(self, number, row, column):
        self.sudoku_9.board[row][column] = number
        self.assertFalse(self.sudoku_9.validate_rows(self.sudoku_9.board))

    def test_winning_nine_9(self):
        sudoku = Sudoku([["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                         ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                         ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                         ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                         ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                         ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                         ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                         ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                         ["3", "4", "5", "2", "8", "6", "1", "7", "9"]])
        self.assertFalse(sudoku.end_game())

    def test_not_winning_nine_9(self):
        self.assertFalse(self.sudoku_9.end_game())
    
    @parameterized.expand([
        ("8", 7, 2),
        ("4", 0, 3),
        ("7", 6, 4),
        ("9", 0, 5),
        ("2", 0, 6),
        ("6", 7, 7),
        ("7", 0, 2),
        ("5", 1, 7),
        ("6", 2, 3),
        ("8", 3, 6),
        ("4", 4, 4),
        ("7", 5, 6),
        ("6", 6, 3),
        ("9", 7, 0),
        ("8", 8, 1),
        ("5", 8, 0),
        ("3", 8, 1),
        ("9", 0, 8),
        ("3", 2, 0),
        ("9", 0, 3),
        ("6", 0, 8),
        ("7", 3, 2),
        ("2", 3, 5),
        ("6", 3, 6),
        ("6", 8, 0),
        ("9", 8, 3),
        ("8", 8, 6),
    ])
    def test_valid_board_nine_9(self, number, row, column):
        self.sudoku_9.board[row][column] = number
        self.assertFalse(self.sudoku_9.validate_board())
  
if __name__ == '__main__':
    unittest.main()