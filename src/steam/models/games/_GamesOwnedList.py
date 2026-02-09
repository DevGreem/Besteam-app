from pydantic import BaseModel
from . import SimpleOwnedGameInfo, OwnedGameInfo

class BaseGamesOwnedList(BaseModel):
    game_count: int
    games: list

class SimpleGamesOwnedList(BaseGamesOwnedList):
    games: list[SimpleOwnedGameInfo]

class GamesOwnedList(BaseGamesOwnedList):
    games: list[OwnedGameInfo]