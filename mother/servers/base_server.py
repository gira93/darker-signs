from typing import TypedDict
from termcolor import cprint
from system.mail import Mail
from system.dns import Dns
from system.player import Player
from system.utils import show_menu

Email = TypedDict("Email", {"from": str, "to": str, "content": str})
File = TypedDict("File", {"name": str, "content": str})
Article = TypedDict("Article", {"title": str, "content": str})
ChatMessage = TypedDict("ChatMessage", {"op": str, "content": str})

ServerConfig = TypedDict(
    "ServerConfig",
    {
        "name": str,
        "banner": str,
        "contents": list[Email] | list[File] | list[Article] | list[ChatMessage],
        "writable": bool,
        "crashable": bool,
    },
)


class BaseServer:
    def __init__(self, root_path: str, mail: Mail, dns: Dns, player: Player) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns
        self.player = player

    def file_server(self, config: ServerConfig):
        self.__welcome(config["name"], config["banner"])
        print(config["contents"])

    def web_server(self, config: ServerConfig):
        self.__welcome(config["name"], config["banner"])
        options = show_menu()

    def mail_server(self, config: ServerConfig):
        self.__welcome(config["name"], config["banner"])
        print(config["contents"])

    def chat_server(self, config: ServerConfig):
        self.__welcome(config["name"], config["banner"])
        print(config["contents"])

    def gateway_server(self, config: ServerConfig):
        self.__welcome(config["name"], config["banner"])
        print(config["contents"])

    def __welcome(self, server_name: str, banner: str | None = None):
        welcome_message = banner if banner else f"Welcome to {server_name}"
        cprint(welcome_message, "green")
        print()
