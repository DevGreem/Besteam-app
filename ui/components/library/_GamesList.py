from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QScrollArea,
    QSizePolicy
)
from PyQt6.QtCore import Qt, pyqtSignal
import logging
from src import (
    SteamClient,
    AccountManager,
    Signal
)
from src.steam.models.games import GamesOwnedList
from . import GameMiniCard
import logging
from typing import cast

class GameList(QScrollArea):
    
    on_press_game: Signal[int] = cast(Signal[int], pyqtSignal(int))
    games: GamesOwnedList
    
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        
        self.content = QWidget()
        self.list_layout = QVBoxLayout(self.content)
        self.list_layout.addStretch()
        
        self.__search_games()
        self.__load_games()
        
        self.setWidget(self.content)
        logging.debug("Loaded game list")

    def __search_games(self):
        
        steam = SteamClient()
        
        self.games = steam.users.get_owned_games(AccountManager.actual_user_id, True, True)
        logging.debug(self.games)
    
    def __load_games(self):
        
        for game in self.games.games:
            
            game_container = GameMiniCard(game, self)
            game_container.clicked.connect(self.__on_press_game)
            
            self.list_layout.addWidget(game_container)
    
    def __on_press_game(self, game_id: int):
        pass