from dataclasses import dataclass


@dataclass
class Player:
    username: str
    ranking: int = 0


def create_player():
    name = input("Enter your username: ")
    player = Player(username=name)
    print(f"Player has been created: {player.username}")


create_player()
