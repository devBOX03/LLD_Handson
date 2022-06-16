
from tictactoe.v1.strategies.playing_strategy import PlayingStrategy
from tictactoe.v1.models.board import Board
from tictactoe.v1.models.board_cell import BoardCell

class DefaultPlayingStrategy(PlayingStrategy):
    def play(self, board: Board) -> BoardCell:
        return None