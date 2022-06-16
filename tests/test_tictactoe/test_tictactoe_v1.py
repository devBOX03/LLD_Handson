from typing import List
from pytest import fixture

from tictactoe.v1.models.board import Board
from tictactoe.v1.models.board_cell import BoardCell
from tictactoe.v1.models.bot import Bot
from tictactoe.v1.models.game import Game
from tictactoe.v1.models.game_symbol import GameSymbol
from tictactoe.v1.models.human_player import HumanPlayer
from tictactoe.v1.models.player import Player
from tictactoe.v1.models.user import User
from tictactoe.v1.strategies.default_playing_strategy import DefaultPlayingStrategy

@fixture
def user_info() -> dict:
    return {
        "email": "player1@test.in",
        "username": "player1",
        "photo": None
    }

@fixture
def set_up_game(user_info) -> Game:
    game: Game = Game()

    board: Board = Board(row=3, column=3)
    game.board = board

    user: User = User()
    user.email = user_info["email"]
    user.username = user_info["username"]
    user.photo = user_info["photo"]

    human_palyer: HumanPlayer = HumanPlayer()
    human_palyer.game_symbol = GameSymbol.circle
    human_palyer.user = user

    bot: Bot = Bot()
    bot.game_symbol = GameSymbol.cross
    bot.playing_strategy = DefaultPlayingStrategy()

    game.players = [human_palyer, bot]

    return game

def test_board_dimensions(set_up_game):
    game: Game = set_up_game
    game_board: Board = game.board
    board_cells: List[List[BoardCell]] = game_board.cells

    assert len(board_cells) == 3
    assert len(board_cells[0]) == 3

def test_human_player(set_up_game, user_info):
    game: Game = set_up_game
    players: List[Player] = game.players
    human_player: HumanPlayer = players[0]
    user: User = human_player.user

    assert human_player.game_symbol == GameSymbol.circle
    assert user.email == user_info["email"]
