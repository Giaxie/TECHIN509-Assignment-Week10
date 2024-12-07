import unittest
from models.board import Board

class TestCheckWinner(unittest.TestCase):
    def test_row_winner(self):
        board = Board()
        board.board = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        self.assertEqual(board.check_winner(), "X")

    def test_no_winner(self):
        board = Board()
        board.board = [["X", "O", "X"], ["X", "X", "O"], ["O", "X", "O"]]
        self.assertIsNone(board.check_winner())

if __name__ == "__main__":
    unittest.main()
