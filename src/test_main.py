from main import UserPlayer, EasyComputerPlayer, TicTacToe, select_starting_player
from players import RangeError, OccupiedError
import pytest 


user_player_1 = UserPlayer("X", "Dayle")
pete_panda = EasyComputerPlayer("O", "Pete the Panda")
standard_board = TicTacToe()

def fake_input(monkeypatch, user_input):
    test_inputs = iter(user_input)
    monkeypatch.setattr("builtins.input", lambda prompt: next(test_inputs))

class TestGetMove:

    def test_get_move(self, monkeypatch):
        fake_input(monkeypatch,[0, 5, 8])
        assert user_player_1.get_move(standard_board) == 0
        assert user_player_1.get_move(standard_board) == 5
        assert user_player_1.get_move(standard_board) == 8

    def test_above_range(self, monkeypatch):
        fake_input(monkeypatch,[-1, -20, -50])
        for i in range(3):
            with pytest.raises(RangeError):
                user_player_1.get_move(standard_board)

    def test_below_range(self, monkeypatch):
        fake_input(monkeypatch,[9, 20, 50])
        for i in range(3):
            with pytest.raises(RangeError):
                user_player_1.get_move(standard_board)

    def test_string(self, monkeypatch):
        fake_input(monkeypatch,["three", "five", "eight"])
        with pytest.raises(ValueError):
            user_player_1.get_move(standard_board)

    def test_float(self, monkeypatch):
        fake_input(monkeypatch,["-0.5", "0.8", "1.5"])
        with pytest.raises(ValueError):
            user_player_1.get_move(standard_board)
    
    def test_occupied_error(self, monkeypatch):
        standard_board.board = ["O", " ", "X", " ", "X", " ", "X", " ", "O"]
        fake_input(monkeypatch,[0, 2, 4])
        with pytest.raises(OccupiedError):
            user_player_1.get_move(standard_board)

class TestWinner:

    def test_winner_diagonal(self):         
        assert standard_board.winner(4, "X") is True
        standard_board.board = ["O", " ", "", " ", "O", " ", "X", " ", "O"]
        assert standard_board.winner(2, "X") is False
        standard_board.board = ["O", " ", "X", " ", "O", " ", "X", " ", "O"]
        assert standard_board.winner(4, "O") is True
        standard_board.board = [" ", "X", "X", " ", "O", " ", "X", " ", "O"]
        assert standard_board.winner(0, "O") is False
    
    def test_winner_rows(self):         
        standard_board.board = ["X", "X", "X", " ", "O", " ", " ", " ", "O"]
        assert standard_board.winner(1, "X") is True
        standard_board.board = ["X", " ", "X", " ", "O", " ", "X", " ", "O"]
        assert standard_board.winner(1, "X") is False
        standard_board.board = ["X", " ", "X", "O", "O", "O", " ", " ", "X"]
        assert standard_board.winner(3, "O") is True
        standard_board.board = ["X", " ", "X", "O", "X", "O", " ", "O", "X"]
        assert standard_board.winner(3, "O") is False

    def test_winner_columns(self):         
        standard_board.board = ["X", " ", " ", "X", "O", " ", "X", " ", "O"]
        assert standard_board.winner(0, "X") is True
        standard_board.board = ["O", " ", " ", "X", "O", " ", "X", " ", "O"]
        assert standard_board.winner(0, "X") is False
        standard_board.board = ["X", "O", " ", "X", "O", " ", " ", "O", "X"]
        assert standard_board.winner(1, "O") is True
        standard_board.board = ["X", "O", " ", "X", "X", " ", "O", "O", "X"]
        assert standard_board.winner(1, "O") is False

class TestWinner: