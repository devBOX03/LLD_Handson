from tictactoe.v1.models.game_symbol import GameSymbol

class BoardCell(object):
    def __init__(self):
        self._row: int = None
        self._column: int = None
        self._game_symbol: GameSymbol = None

    @property
    def row(self) -> int:
        return self._row

    @row.setter
    def row(self, row: int) -> None:
        self._row = row

    @property
    def column(self) -> int:
        return self._column

    @column.setter
    def column(self, column: int) -> None:
        self._column = column

    @property
    def game_symbol(self) -> GameSymbol:
        return self._game_symbol

    @game_symbol.setter
    def game_symbol(self, game_symbol: GameSymbol) -> None:
        self._game_symbol = game_symbol
