import json


class Player:
    def __init__(self, player_file: str) -> None:
        with open(player_file, "r") as f:
            self.player: dict = json.load(f)
