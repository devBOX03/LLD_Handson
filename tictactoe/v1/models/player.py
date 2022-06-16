import abc

from tictactoe.v1.models.board import Board
from tictactoe.v1.models.board_cell import BoardCell
from tictactoe.v1.models.game_symbol import GameSymbol

class Player(abc.ABC):
    @property
    @abc.abstractmethod
    def game_symbol(self) -> GameSymbol:
        ...
    
    @abc.abstractmethod
    def play(self, board: Board) -> BoardCell:
        ...
