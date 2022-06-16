import abc
from typing import List
from tictactoe.v2.models.board import Board
from tictactoe.v2.models.player import Player

class WinningStrategy(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def check_winner(self, board: Board, players: List[Player]) -> Player:
        ...
