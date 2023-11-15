import pytest
from board import TicTacToeBoard


def test_board_creation():
    board = TicTacToeBoard()
    assert board is not None


def test_play_o_on_empty_board():
    board = TicTacToeBoard()
    assert pytest.raises(ValueError, board.play_o, (0, 0))


def test_play_x_on_empty_board():
    board = TicTacToeBoard()
    board.play_x((0, 0))
    board.play_o((1, 1))


def test_play_round():
    board = TicTacToeBoard()
    board.play_x((0, 0))
    board.play_o((1, 1))


def test_play_move_on_occupied_tile():
    board = TicTacToeBoard()
    board.play_x((0, 0))
    pytest.raises(ValueError, board.play_o, (0, 0))


def test_play_move_off_board_tile():
    board = TicTacToeBoard()
    pytest.raises(ValueError, board.play_x, (0, -1))
