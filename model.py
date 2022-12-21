from dataclasses import dataclass


@dataclass
class Player:
    name: str
    score: int

    def save_player(self):
        return {self.name: self.score}

