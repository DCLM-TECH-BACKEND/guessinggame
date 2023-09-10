from dataclasses import dataclass


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



def create_player():
    name = input("Enter your username: ")
    player = Player(username=name)
    print(f"Player has been created: {player.username}")


if __name__ == "__main__":
    create_player()
