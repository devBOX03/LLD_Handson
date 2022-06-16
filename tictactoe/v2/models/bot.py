from tictactoe.v2.models.board import Board
from tictactoe.v2.models.board_cell import BoardCell
from tictactoe.v2.models.player import Player
from tictactoe.v2.models.game_symbol import GameSymbol
from tictactoe.v2.strategies.playing_strategy import PlayingStrategy

class Bot(Player):
    def __init__(self):
        self._game_symbol: GameSymbol = None
        self._playing_strategy: PlayingStrategy = None

    @property
    def game_symbol(self) -> GameSymbol:
        return self._game_symbol

    @property
    def playing_strategy(self) -> PlayingStrategy:
        return self._playing_strategy

    def play(self, board: Board) -> BoardCell:
        return BoardCell()

    @classmethod
    def get_builder(cls):
        return cls.BotBuilder()

    class BotBuilder:
        def __init__(self):
            self._bot: Bot = Bot()

        def with_symbol(self, symbol: GameSymbol):
            self._bot._game_symbol = symbol
            return self

        def with_playing_strategy(self, playing_strategy: PlayingStrategy):
            self._bot._playing_strategy = playing_strategy
            return self

        def _validate(self):
            if self._bot._game_symbol not in GameSymbol:
                raise Exception("Bot game symbol is not valid!")
            if not isinstance(self._bot._playing_strategy, PlayingStrategy):
                raise TypeError("Bot playing strategy is not valid!")

        def build(self):
            self._validate()
            return self._bot
