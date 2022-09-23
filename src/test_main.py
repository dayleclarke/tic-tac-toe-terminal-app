from main import UserPlayer, TicTacToe
from players import RangeError, OccupiedError
import pytest 

inputs = iter([0, 5, 8, 9, 20, 50, -1, -20, -50, "three", 0.5])
user_player_1 = UserPlayer("X", "Dayle")
standard_board = TicTacToe()

def fake_input(prompt):
    return next(inputs)

class TestGetMove:
    def test_get_move(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_input)
        assert user_player_1.get_move(standard_board) == 0
        assert user_player_1.get_move(standard_board) == 5
        assert user_player_1.get_move(standard_board) == 8
    
    def test_above_range(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_input)
        for i in range(3):
            with pytest.raises(RangeError):
                user_player_1.get_move(standard_board)
    
    def test_below_range(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_input)
        for i in range(3):
            with pytest.raises(RangeError):
                user_player_1.get_move(standard_board)
    
    def test_string(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_input)
        with pytest.raises(ValueError):
            user_player_1.get_move(standard_board)
    
    def test_float(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_input)
        with pytest.raises(ValueError):
            user_player_1.get_move(standard_board)
    
    # def test_float(self, monkeypatch):
    #     monkeypatch.setattr("builtins.input", fake_input)
    #     with pytest.raises(ValueError):
    #         user_player_1.get_move(standard_board)    
    
    # def test_below_range(self, monkeypatch):
    #     monkeypatch.setattr("builtins.input", fake_input)
    #     with pytest.raises(RangeError):  
    #         user_player_1.get_move(standard_board)
    #     with pytest.raises(RangeError):  
    #         user_player_1.get_move(standard_board)
    #     with pytest.raises(RangeError):  
    #         user_player_1.get_move(standard_board)