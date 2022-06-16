
from tictactoe.v1.models.board import Board
from tictactoe.v1.models.board_cell import BoardCell
from tictactoe.v1.models.game_symbol import GameSymbol
from tictactoe.v1.models.player import Player
from tictactoe.v1.models.user import User

class HumanPlayer(Player):
    def __init__(self):
        self._game_symbol = None
        self._user:User = None
    
    @property
    def user(self) -> User:
        return self._user
    @user.setter
    def user(self, user: User) -> None:
        self._user = user
    
    @property
    def game_symbol(self) -> GameSymbol:
        return self._game_symbol
    @game_symbol.setter
    def game_symbol(self, game_symbol: GameSymbol) -> None:
        self._game_symbol = game_symbol

    def play(self, board: Board) -> BoardCell:
        return super().play(board)
