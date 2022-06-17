from tictactoe.v2.models.bot import Bot
from tictactoe.v2.models.human_player import HumanPlayer

class PlayerFactory(object):
    @classmethod
    def get_human_player(cls) -> HumanPlayer.HumanPlayerBuilder:
        return HumanPlayer.get_builder()

    @classmethod
    def get_bot_player(cls) -> Bot.BotBuilder:
        return Bot.get_builder()
