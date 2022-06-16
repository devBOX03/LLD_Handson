from typing import List

from tictactoe.v2.models.board import Board
from tictactoe.v2.models.player import Player
from tictactoe.v2.strategies.winning_strategy import WinningStrategy


class Game(object):
    def __init__(self):
        self._board: Board = None
        self._players: List[Player] = list()
        self._winning_strategy: WinningStrategy = None
    
    @property
    def board(self) -> Board:
        return self._board

    @property
    def players(self) -> List[Player]:
        return self._players

    @property
    def winning_strategy(self) -> WinningStrategy:
        return self._winning_strategy

    @classmethod
    def get_builder(cls):
        return cls.GamePlayerBuilder()

    class GamePlayerBuilder:
        def __init__(self):
            self._game: Game = Game()

        def with_board(self, row: int, column: int):
            board: Board = Board(row=row, column=column)
            self._game._board = board
            return self

        def with_player(self, player: Player):
            self._game._players.append(player)
            return self

        def _validate(self):
            if not (len(self._game._players) == 2):
                raise Exception("Two players needed for the game, please check players again!")

        def build(self):
            self._validate()
            return self._game
