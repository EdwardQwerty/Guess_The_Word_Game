from enum import Enum


class GameStatus(Enum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    WIN = 3
    LOST = 4
    STOP = 5