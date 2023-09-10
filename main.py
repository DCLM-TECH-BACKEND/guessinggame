from dataclasses import dataclass
from random import randint


@dataclass
class Player:
    player_id: int
    username: str
    ranking: int = 0
    games_won: int = 0


@dataclass
class GameSession:
    player_1: Player
    player_2: Player
    scores: dict

    def create_session(self):
        pass
    
    def play_game(self):
        pass


def create_player():
    name = input("Enter your username: ")
    player_id = randint(1, 999)
    player = Player(player_id=player_id, username=name)
    print(f"Player has been created: {player.username}")
    return player


if __name__ == "__main__":
    create_player()
