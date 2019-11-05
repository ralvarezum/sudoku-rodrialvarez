import unittest
import io
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from Interfaz_Sudoku import Interface
from api import api
from Sudoku import Sudoku


"""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////"""
"""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////"""
"""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////"""
"""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////""""""//////////INTERFACE////////"""


class TestInterfaceSudoku(unittest.TestCase):

    def setUp(self):
        list_4 = [["4", "x", "3", "1"],
                  ["x", "3", "x", "x"],
                  ["3", "1", "x", "2"],
                  ["x", "4", "x", "x"]]
        self.user_4 = Interface()
        mock = MagicMock()
        mock.side_effect = ["4", "1"]
        with patch("builtins.input", new=mock), patch("Interfaz_Sudoku.api",return_value=list_4):
            self.user_4.start()

        list_9 = [
                    ["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                    ["6", "x", "x", "x", "9", "5", "x", "x", "x"],
                    ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                    ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                    ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                    ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                    ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                    ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                    ["x", "x", "x", "x", "8", "x", "x", "7", "9"]]

        self.user_9 = Interface()
        mock = MagicMock()
        mock.side_effect = ["9", "1"]
        with patch("Interfaz_Sudoku.api",
                   return_value=list_9
                   ), patch(
                   "builtins.input",
                   new=mock
                   ):
            self.user_9.start()


    @parameterized.expand([
        ("b", "4", "6"),
        ("2", "h", "6"),
        ("2", "4", "i"),
        ("@", "4", "6"),
        ("2", "@", "6"),
        ("2", "4", "@"),
        ("@", "4", "+"),
        ("@", "d", "6"),
        ("3", "hola", "*"),
        ("*", "@", "r")
    ])
    def test_check_user_inputs_letters_and_simbols(self, user_number, user_row, user_column):
        result = self.user_4.check_user_inputs(user_number, user_row, user_column)
        self.assertFalse(result)

    def test_check_user_inputs_letter_x_right_number(self):
        result = self.user_4.check_user_inputs("x", 1, 1)
        self.assertTrue(result)

    def test_get_size_4(self):
        with patch("builtins.input", return_value="4"):
            self.user_4.get_size()
        self.assertEqual(self.user_4.size, "4")


    @parameterized.expand([
        ("5"),
        ("r"),
        ("@"),
        ("*"),
        ("129"),
        ("118192")
    ])
    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_get_wrong_size(self, WrongSize, mock_stdout):
        mock = MagicMock()
        mock.side_effect = [WrongSize, "4"]
        with patch("builtins.input", new=mock):
            self.user_4.get_size()
        self.assertEqual(mock_stdout.getvalue(), "Ese tamaño no esta disponible. Las opciones son 4 o 9. Por favor, vuelva a intentar! \n\n\n")

    @parameterized.expand([
        ("2", "0", "1"),
        ("2", "-5", "1"),
        ("2", "5", "1"),
        ("2", "10", "1"),
        ("2", "200", "1"),
        ("2", "10000", "1"),
    ])
    def test_get_wrong_row_4(self, user_number, user_row, user_column):
        mock = MagicMock()
        mock.side_effect = [user_number, user_row, user_column]
        with patch("builtins.input", new=mock):
            result = self.user_4.user_inputs()
        self.assertEqual(result, "\nHa ingresado un numero,fila o columna invalido/a!")

    @parameterized.expand([
        ("2", "1", "0"),
        ("2", "1", "-5"),
        ("2", "1", "5"),
        ("2", "1", "10"),
        ("2", "1", "200"),
        ("2", "1", "10000"),
    ])
    def test_get_wrong_column_4(self, user_number, user_row, user_column):
        mock = MagicMock()
        mock.side_effect = [user_number, user_row, user_column]
        with patch("builtins.input", new=mock):
            result = self.user_4.user_inputs()
        self.assertEqual(result, "\nHa ingresado un numero,fila o columna invalido/a!")

    @parameterized.expand([
        ("0", "2", "1"),
        ("-7", "2", "1"),
        ("6", "2", "1"),
        ("10", "2", "1"),
        ("3000", "2", "1"),
    ])
    def test_get_wrong_numbers_4(self, user_number, user_row, user_column):
        mock = MagicMock()
        mock.side_effect = [user_number, user_row, user_column]
        with patch("builtins.input", new=mock):
            result = self.user_4.user_inputs()
        self.assertEqual(result, "\nHa ingresado un numero,fila o columna invalido/a!")

    @parameterized.expand([
        ("2", "1", "2"),
        ("4", "3", "3"),
        ("1", "2", "1"),
        ("2", "4", "1"),
        ("2", "2", "3"),
        ("4", "2", "4"),
        ("1", "4", "3"),
        ("3", "4", "4"),
    ])
    def test_get_good_number_row_column_4(self, user_number, user_row, user_column):
        mock = MagicMock()
        mock.side_effect = [user_number, user_row, user_column]
        with patch("builtins.input", new=mock):
            result = self.user_4.user_inputs()
        self.assertNotEqual(result, "\nHa ingresado un numero,fila o columna invalido/a!")

    def test_get_size_9(self):
        with patch("builtins.input", return_value="9"):
            self.user_9.get_size()
        self.assertEqual(self.user_9.size, "9")

    @parameterized.expand([
        ("4", "1", "3"),
        ("6", "1", "4"),
        ("8", "1", "6"),
        ("9", "1", "7"),
        ("1", "1", "8"),
        ("2", "1", "9"),
        ("7", "2", "2"),
        ("2", "2", "3"),
        ("1", "2", "4"),
        ("3", "2", "7"),
        ("4", "2", "8"),
        ("8", "2", "9"),
        ("1", "3", "1"),
        ("3", "3", "4"),
        ("4", "3", "5"),
        ("2", "3", "6"),
        ("5", "3", "7"),
        ("7", "3", "9"),
        ("5", "4", "2"),
        ("9", "4", "3"),
        ("7", "4", "4"),
        ("1", "4", "6"),
        ("4", "4", "7"),
        ("2", "4", "8"),
        ("2", "5", "2"),
        ("6", "5", "3"),
        ("5", "5", "5"),
        ("7", "5", "7"),
        ("9", "5", "8"),
        ("1", "6", "2"),
        ("3", "6", "3"),
        ("9", "6", "4"),
        ("4", "6", "6"),
        ("8", "6", "7"),
        ("5", "6", "8"),
        ("9", "7", "1"),
        ("1", "7", "3"),
        ("5", "7", "4"),
        ("3", "7", "5"),
        ("7", "7", "6"),
        ("4", "7", "9"),
        ("2", "8", "1"),
        ("8", "8", "2"),
        ("7", "8", "3"),
        ("6", "8", "7"),
        ("3", "8", "8"),
        ("3", "9", "1"),
        ("4", "9", "2"),
        ("5", "9", "3"),
        ("2", "9", "4"),
        ("6", "9", "6"),
        ("1", "9", "7"),
    ])
    def test_get_good_number_row_column_9(self, user_number, user_row, user_column):
        mock = MagicMock()
        mock.side_effect = [user_number, user_row, user_column]
        with patch("builtins.input", new=mock):
            result = self.user_9.user_inputs()
        self.assertNotEqual(result, "\nHa ingresado un numero,fila o columna invalido/a!")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_play_win_4(self, mock_stdout):

        mock = MagicMock()
        mock.side_effect = ["2", "1", "2",
                            "4", "3", "3",
                            "1", "2", "1",
                            "2", "4", "1",
                            "2", "2", "3",
                            "4", "2", "4",
                            "1", "4", "3",
                            "3", "4", "4"]
        with patch("Interfaz_Sudoku.Interface.start",
                   return_value=None), patch("builtins.input", new=mock):
            self.user_4.play()
        self.assertEqual(mock_stdout.getvalue()[-11:], "\n\nYOU WIN!\n")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_play_win_9(self, mock_stdout):

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
                            "8", "8", "2",
                            "7", "8", "3",
                            "6", "8", "7",
                            "3", "8", "8",
                            "3", "9", "1",
                            "4", "9", "2",
                            "5", "9", "3",
                            "2", "9", "4",
                            "6", "9", "6",
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
        self.sudoku9 = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                               ["6", "x", "x", "x", "9", "5", "x", "x", "x"],
                               ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                               ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                               ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                               ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                               ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                               ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                               ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.sudoku4 = Sudoku([["4", "x", "3", "1"],
                               ["x", "3", "x", "x"],
                               ["3", "1", "x", "2"],
                               ["x", "4", "x", "x"]])

    def test_correct_board_9(self):
        self.assertTrue(self.sudoku9.validate_board())

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
    def test_wrong_numbers_9(self, user_number, user_row, user_column):
        result = self.sudoku9.set_number(user_number, user_row, user_column)
        self.assertEqual(result,"No puede ingresar un numero en esa coordenada!")

    @parameterized.expand([
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
        (6, 4, 2),
        (5, 4, 4),
        (7, 4, 6),
        (9, 4, 7),
        (1, 5, 1),
        (3, 5, 2),
        (9, 5, 3),
        (4, 5, 5),
        (8, 5, 6),
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
        (3, 8, 0),
        (4, 8, 1),
        (5, 8, 2),
        (2, 8, 3),
        (6, 8, 5),
        ("x", 8, 2),
        ("x", 8, 3),
        ("x", 8, 5),
        ("x", 8, 6),
        (1, 8, 6),
    ])
    def test_good_numbers_9(self, user_number, user_row, user_column):
        result = self.sudoku9.set_number(user_number, user_row, user_column)
        self.assertNotEqual(result,"No puede ingresar un numero en esa coordenada!")

    @parameterized.expand([
        ("7", 0, 2),
        ("5", 1, 7),
        ("6", 2, 3),
        ("8", 3, 6),
        ("4", 4, 4),
        ("7", 5, 6),
        ("6", 6, 3),
        ("9", 7, 0),
        ("8", 8, 1),
        ])
    def test_validate_board_rows_9(self, user_number, user_row, user_column):
        self.sudoku9.board[user_row][user_column] = user_number
        self.assertFalse(self.sudoku9.validate_rows(self.sudoku9.board))

    @parameterized.expand([
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
        ("8", 7, 2),
        ("4", 0, 3),
        ("7", 6, 4),
        ("9", 0, 5),
        ("2", 0, 6),
        ("6", 7, 7),
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
    def test_validate_board_9(self, user_number, user_row, user_column):
        self.sudoku9.board[user_row][user_column] = user_number
        self.assertFalse(self.sudoku9.validate_board())

    def test_not_winning_9(self):
        self.assertFalse(self.sudoku9.win())

    def test_winning_9(self):
        sudoku = Sudoku([["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                         ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                         ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                         ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                         ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                         ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                         ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                         ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                         ["3", "4", "5", "2", "8", "6", "1", "7", "9"]])
        self.assertTrue(sudoku.win())

    @parameterized.expand([
        ("4", 0, 1),
        ("3", 0, 1),
        ("4", 1, 0),
        ("3", 1, 0),
        ("1", 3, 0),
        ("1", 1, 2),
        ("2", 3, 2),
        ("3", 0, 1),
        ("3", 1, 3),
        ("1", 2, 2),
        ("4", 3, 3),
        ("4", 3, 0),
        ("3", 1, 0),
        ("4", 0, 1),
        ("1", 0, 1),
        ("3", 3, 2),
        ("1", 3, 3),
        ("2", 1, 3)
    ])
    def test_validate_board_4(self, number, row, column):
        self.sudoku4.board[row][column] = number
        self.assertFalse(self.sudoku4.validate_board())

    def test_correct_board_4(self):
        self.assertTrue(self.sudoku4.validate_board())

    @parameterized.expand([
        (4, 0, 1),
        (3, 0, 1),
        (4, 1, 0),
        (3, 1, 0),
        (1, 3, 0),
        (1, 1, 2),
        (2, 3, 2)
    ])
    def test_set_numbers_quadrant_4(self, number, row, column):
        result = self.sudoku4.set_number(number, row, column)
        self.assertEqual(result, "No puede ingresar un numero en esa coordenada!")

    @parameterized.expand([
        (3, 0, 1),
        (3, 1, 3),
        (1, 2, 2),
        (4, 3, 3)
    ])
    def test_set_numbers_same_row_4(self, number, row, column):
        result = self.sudoku4.set_number(number, row, column)
        self.assertEqual(result, "No puede ingresar un numero en esa coordenada!")

    @parameterized.expand([
        (4, 3, 0),
        (3, 1, 0),
        (4, 0, 1),
        (1, 0, 1),
        (3, 3, 2),
        (1, 3, 3),
        (2, 1, 3)
    ])
    def test_set_numbers_same_column_4(self, number, row, column):
        result = self.sudoku4.set_number(number, row, column)
        self.assertEqual(result, "No puede ingresar un numero en esa coordenada!")

    @parameterized.expand([
        (2, 0, 1),
        (4, 2, 2),
        (1, 1, 0),
        (2, 3, 0),
        (2, 1, 2),
        (4, 1, 3),
        (1, 3, 2),
        ("x", 1, 2),
        ("x", 1, 3),
        ("x", 3, 2),
        (3, 3, 3),
    ])
    def test_set_good_value_4(self, number, row, column):
        result = self.sudoku4.set_number(number, row, column)
        self.assertNotEqual(result, "No puede ingresar un numero en esa coordenada!")

    def test_not_winning_4(self):
        self.assertFalse(self.sudoku4.win())

    def test_winning_4(self):
        sudoku = Sudoku([["4", "2", "3", "1"],
                         ["1", "3", "2", "4"],
                         ["3", "1", "4", "2"],
                         ["2", "4", "1", "3"]])

        self.assertTrue(sudoku.win())


"""//////////API////////""""""//////////API////////""""""//////////API////////""""""//////////API////////"""
"""//////////API////////""""""//////////API////////""""""//////////API////////""""""//////////API////////"""
"""//////////API////////""""""//////////API////////""""""//////////API////////""""""//////////API////////"""
"""//////////API////////""""""//////////API////////""""""//////////API////////""""""//////////API////////"""

class TestAPISudoku(unittest.TestCase):

    def test_api_size_9_1(self):
        mock_response = MagicMock()
        mock_response.json = MagicMock(return_value={
                                "response": True,
                                "size": "9",
                                "squares": [
                                    {"x": 0, "y": 1, "value": 6},
                                    {"x": 0, "y": 7, "value": 1},
                                    {"x": 0, "y": 8, "value": 2},
                                    {"x": 1, "y": 1, "value": 2},
                                    {"x": 1, "y": 4, "value": 3},
                                    {"x": 1, "y": 5, "value": 9},
                                    {"x": 1, "y": 7, "value": 5},
                                    {"x": 1, "y": 8, "value": 6},
                                    {"x": 2, "y": 1, "value": 7},
                                    {"x": 2, "y": 2, "value": 4},
                                    {"x": 2, "y": 5, "value": 6},
                                    {"x": 2, "y": 6, "value": 3},
                                    {"x": 3, "y": 0, "value": 4},
                                    {"x": 3, "y": 3, "value": 6},
                                    {"x": 3, "y": 4, "value": 2},
                                    {"x": 3, "y": 5, "value": 8},
                                    {"x": 3, "y": 8, "value": 9},
                                    {"x": 4, "y": 0, "value": 7},
                                    {"x": 4, "y": 2, "value": 6},
                                    {"x": 4, "y": 4, "value": 5},
                                    {"x": 4, "y": 6, "value": 2},
                                    {"x": 4, "y": 8, "value": 3},
                                    {"x": 5, "y": 0, "value": 9},
                                    {"x": 5, "y": 3, "value": 4},
                                    {"x": 5, "y": 8, "value": 5},
                                    {"x": 6, "y": 0, "value": 2},
                                    {"x": 6, "y": 2, "value": 5},
                                    {"x": 6, "y": 3, "value": 1},
                                    {"x": 6, "y": 6, "value": 9},
                                    {"x": 6, "y": 7, "value": 8},
                                    {"x": 7, "y": 1, "value": 9},
                                    {"x": 7, "y": 3, "value": 3},
                                    {"x": 7, "y": 4, "value": 8},
                                    {"x": 7, "y": 6, "value": 5},
                                    {"x": 7, "y": 7, "value": 2},
                                    {"x": 8, "y": 1, "value": 4},
                                    {"x": 8, "y": 2, "value": 1},
                                    {"x": 8, "y": 4, "value": 9},
                                    {"x": 8, "y": 6, "value": 6},
                                    {"x": 8, "y": 7, "value": 3}]})

        with patch("api.requests.get", return_value=mock_response):
            res = api(9)
        self.assertEqual(res, [["x", "x", "x", "4", "7", "9", "2", "x", "x"],
                               ["6", "2", "7", "x", "x", "x", "x", "9", "4"],
                               ["x", "x", "4", "x", "6", "x", "5", "x", "1"],
                               ["x", "x", "x", "6", "x", "4", "1", "3", "x"],
                               ["x", "3", "x", "2", "5", "x", "x", "8", "9"],
                               ["x", "9", "6", "8", "x", "x", "x", "x", "x"],
                               ["x", "x", "3", "x", "2", "x", "9", "5", "6"],
                               ["1", "5", "x", "x", "x", "x", "8", "2", "3"],
                               ["2", "6", "x", "9", "3", "5", "x", "x", "x"]])

    def test_api_size_4_1(self):
        mock_response = MagicMock()
        mock_response.json = MagicMock(return_value={
                                "response": True,
                                "size": "4",
                                "squares": [
                                    {"x": 0, "y": 0, "value": 4},
                                    {"x": 0, "y": 2, "value": 3},
                                    {"x": 0, "y": 3, "value": 1},
                                    {"x": 1, "y": 1, "value": 3},
                                    {"x": 2, "y": 0, "value": 3},
                                    {"x": 2, "y": 1, "value": 1},
                                    {"x": 2, "y": 3, "value": 2},
                                    {"x": 3, "y": 1, "value": 4}]})

        with patch("api.requests.get", return_value=mock_response):
            res = api(4)
        self.assertEqual(res, [["4", "x", "3", "x"],
                               ["x", "3", "1", "4"],
                               ["3", "x", "x", "x"],
                               ["1", "x", "2", "x"]])


if __name__ == '__main__':
    unittest.main()