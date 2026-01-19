

class InvalidUserId(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__("You cannot introduce a user with id 0 or less!", *args)