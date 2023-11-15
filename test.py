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
    pytest.raises(ValueError, board.play_x, (0, TicTacToeBoard.num_cols))
    pytest.raises(ValueError, board.play_x, (-1, 0))
    pytest.raises(ValueError, board.play_x, (TicTacToeBoard.num_rows, 0))


def test_row_win():
    board = TicTacToeBoard()
    assert not board.check_x_win()
    board.play_x((0, 0))
    assert not board.check_x_win()
    board.play_o((0, 1))
    assert not board.check_x_win()
    board.play_x((1, 0))
    assert not board.check_x_win()
    board.play_o((1, 1))
    assert not board.check_x_win()
    board.play_x((2, 0))
    assert board.check_x_win()


def test_backward_diagonal_win():
    board = TicTacToeBoard()
    assert not board.check_x_win()
    board.play_x((0, 0))
    assert not board.check_x_win()
    board.play_o((0, 1))
    assert not board.check_x_win()
    board.play_x((1, 1))
    assert not board.check_x_win()
    board.play_o((1, 0))
    assert not board.check_x_win()
    board.play_x((2, 2))
    assert board.check_x_win()
