from tictactoe.v1.models.board import Board
from tictactoe.v1.models.board_cell import BoardCell
from tictactoe.v1.models.player import Player
from tictactoe.v1.models.game_symbol import GameSymbol
from tictactoe.v1.strategies.playing_strategy import PlayingStrategy

class Bot(Player):
    def __init__(self):
        self._game_symbol: GameSymbol = None
        self._playing_strategy: PlayingStrategy = None

    @property
    def game_symbol(self) -> GameSymbol:
        return self._game_symbol

    @game_symbol.setter
    def game_symbol(self, game_symbol: GameSymbol) -> None:
        self._game_symbol = game_symbol

    @property
    def playing_strategy(self) -> PlayingStrategy:
        return self._playing_strategy

    @playing_strategy.setter
    def playing_strategy(self, playing_strategy: PlayingStrategy) -> None:
        self._playing_strategy = playing_strategy

    def play(self, board: Board) -> BoardCell:
        return BoardCell()
