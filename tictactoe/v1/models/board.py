
from typing import List
from tictactoe.v1.models.board_cell import BoardCell

class Board(object):
    def __init__(self, row: int, column: int):
        self._cells: List[List[BoardCell]] = [[BoardCell() for _ in range(column)]for _ in range(row)]

    @property
    def cells(self) -> List[List[BoardCell]]:
        return self._cells

    @cells.setter
    def cells(self, cells: List[List[BoardCell]]) -> None:
        self._cells = cells
