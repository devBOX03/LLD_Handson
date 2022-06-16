import abc

from tictactoe.v1.models.board import Board
from tictactoe.v1.models.board_cell import BoardCell

class PlayingStrategy(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def play(self, board: Board) -> BoardCell:
        ...
