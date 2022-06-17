from typing import List
from pytest import fixture

from tictactoe.v2.factories.player_factory import PlayerFactory
from tictactoe.v2.models.board import Board
from tictactoe.v2.models.board_cell import BoardCell
from tictactoe.v2.models.bot import Bot
from tictactoe.v2.models.game import Game
from tictactoe.v2.models.game_symbol import GameSymbol
from tictactoe.v2.models.human_player import HumanPlayer
from tictactoe.v2.models.player import Player
from tictactoe.v2.models.user import User
from tictactoe.v2.strategies.default_playing_strategy import DefaultPlayingStrategy

@fixture
def user_info() -> dict:
    return {
        "email": "player1@test.in",
        "username": "player1",
        "photo": None
    }

@fixture
def set_up_game(user_info) -> Game:
    game: Game
    bot: Bot
    human_palyer: HumanPlayer

    human_palyer = PlayerFactory.get_human_player() \
                                .with_symbol(GameSymbol.circle) \
                                .with_user_info(User(email=user_info["email"],
                                                   username=user_info["username"],
                                                   photo=user_info["photo"])) \
                                .build()

    bot = PlayerFactory.get_bot_player() \
                       .with_symbol(GameSymbol.cross) \
                       .with_playing_strategy(DefaultPlayingStrategy()) \
                       .build()

    game = Game.get_builder() \
               .with_board(row=3, column=3) \
               .with_player(human_palyer) \
               .with_player(bot) \
               .build()

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
