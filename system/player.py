import json
from typing import TypedDict


class PlayerStatus(TypedDict):
    campaign: str
    balance: int
    experience: int
    tools: list[str]
    active_mission: str | None
    completed_missions: list[str]
    pinned_servers: list[list[str]]
    changed_servers: dict[str, dict]


class Player:
    def __init__(self, player_file: str) -> None:
        self.player_file = player_file
        with open(self.player_file, "r") as f:
            self.player: PlayerStatus = json.load(f)

    def balance(self) -> int:
        return self.player["balance"]

    def add_credit(self, amount: int) -> None:
        self.player["balance"] += amount
        self.__save()

    def subtract_credit(self, amount: int) -> None:
        self.player["balance"] -= amount
        if self.player["balance"] < 0:
            self.player["balance"] = 0
        self.__save()

    def experience(self) -> int:
        return self.player["experience"]

    def add_experience(self, amount: int) -> None:
        self.player["experience"] += amount
        self.__save()

    def tools(self) -> list[str]:
        return self.player["tools"]

    def add_tool(self, tool: str) -> None:
        self.player["tools"].append(tool)
        self.__save()

    def has_tool(self, tool: str) -> bool:
        return tool in self.player["tools"]

    def active_mission(self) -> str | None:
        return self.player["active_mission"]

    def completed_missions(self) -> list[str]:
        return list(self.player["completed_missions"])

    def set_active_mission(self, id: str | None) -> None:
        self.player["active_mission"] = id
        self.__save()

    def add_completed_mission(self, id: str) -> None:
        self.player["completed_missions"].append(id)
        self.player["completed_missions"] = list(set(self.player["completed_missions"]))
        self.__save()

    def pinned_servers(self) -> list[tuple[str, str]]:
        servers: list[tuple[str, str]] = []

        for server in self.player["pinned_servers"]:
            servers.append((server[0], server[1]))

        return servers

    def add_pin_server(self, server: str, port: str) -> None:
        pass

    def get_server(self, id: str) -> dict | None:
        try:
            return self.player["changed_servers"][id]
        except KeyError:
            return None

    def add_or_update_server(self, id: str, server_config: dict) -> None:
        self.player["changed_servers"][id] = server_config
        self.__save()

    def __save(self) -> None:
        with open(self.player_file, "w") as f:
            json.dump(self.player, f, indent="\t")
