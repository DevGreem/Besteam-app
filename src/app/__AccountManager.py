from functools import lru_cache
from PyQt6.QtCore import QObject
from src import Signal, InvalidUserId
from src.steam.models.users import Player
from typing import overload
import logging

class AccountManager(QObject):
    
    __actual_user_id: str = ""
    on_user_logged: Signal[str] = Signal.create(str)
    on_user_logout: Signal[str] = Signal.create(str)
    
    @property
    def actual_user_id(self) -> str:
        return self.__actual_user_id
    
    @overload
    def login_user(self, new_user_id: str): ...
    
    @overload
    def login_user(self, new_user_id: Player): ...
    
    def login_user(self, new_user_id: str|Player):
        
        user_id: str = ""
        logging.debug(f"Logging user {new_user_id}...")
        
        if isinstance(new_user_id, str):
            if not new_user_id:
                raise InvalidUserId()
            
            user_id = new_user_id
        else:
            if not new_user_id.steamid:
                raise InvalidUserId()
            
            user_id = new_user_id.steamid
        
        self.__actual_user_id = user_id
        logging.debug(f"User {user_id} logged")
        self.on_user_logged.emit(self.actual_user_id)
        
    def logout_user(self):
        
        logging.debug(f"Logouted user {self.actual_user_id}")
        self.on_user_logout.emit(self.actual_user_id)
        self.__actual_user_id = ""

@lru_cache
def get_account_manager() -> AccountManager:
    return AccountManager()