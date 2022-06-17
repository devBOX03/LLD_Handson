
from tictactoe.v2.models.board import Board
from tictactoe.v2.models.board_cell import BoardCell
from tictactoe.v2.models.game_symbol import GameSymbol
from tictactoe.v2.models.player import Player
from tictactoe.v2.models.user import User

class HumanPlayer(Player):
    def __init__(self):
        self._game_symbol = None
        self._user:User = None
    
    @property
    def user(self) -> User:
        return self._user
    
    @property
    def game_symbol(self) -> GameSymbol:
        return self._game_symbol

    def play(self, board: Board) -> BoardCell:
        return BoardCell()

    @classmethod
    def get_builder(cls):
        return cls.HumanPlayerBuilder()

    class HumanPlayerBuilder:
        def __init__(self):
            self._human_player: HumanPlayer = HumanPlayer()

        def with_symbol(self, symbol: GameSymbol):
            self._human_player._game_symbol = symbol
            return self

        def with_user_info(self, user: User):
            self._human_player._user = user
            return self

        def _validate(self):
            if self._human_player._game_symbol not in GameSymbol:
                raise Exception("Bot game symbol is not valid!")

        def build(self):
            self._validate()
            return self._human_player
