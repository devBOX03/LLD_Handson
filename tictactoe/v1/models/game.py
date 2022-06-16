from typing import List

from tictactoe.v1.models.board import Board
from tictactoe.v1.models.player import Player
from tictactoe.v1.strategies.winning_strategy import WinningStrategy


class Game(object):
    def __init__(self):
        self._board: Board = None
        self._players: List[Player] = None
        self._winning_strategy: WinningStrategy = None
    
    @property
    def board(self) -> Board:
        return self._board

    @board.setter
    def board(self, board: Board) -> None:
        self._board = board

    @property
    def players(self) -> List[Player]:
        return self._players

    @players.setter
    def players(self, players: List[Player]) -> None:
        self._players = players

    @property
    def winning_strategy(self) -> WinningStrategy:
        return self._winning_strategy

    @winning_strategy.setter
    def winning_strategy(self, winning_strategy: WinningStrategy) -> None:
        self._winning_strategy = winning_strategy
