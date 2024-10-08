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


class ServerConfig(TypedDict):
    id: str
    banner: str
    writable: bool
    crashable: bool
    crashed: bool
    hackable: str | None


class WebServerConfig(ServerConfig):
    contents: list[Article]


class FileServerConfig(ServerConfig):
    contents: list[File]


class MailServerConfig(ServerConfig):
    contents: list[Email]


class ChatServerConfig(ServerConfig):
    contents: list[ChatMessage]


class BaseServer:
    def __init__(self, root_path: str, mail: Mail, dns: Dns, player: Player) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns
        self.player = player

    def file_server(self, server_config: ServerConfig):
        banner = server_config["banner"]
        self.__welcome(banner)

    def web_server(self, server_config: WebServerConfig):
        id = server_config["id"]
        server_override = self.player.get_server(id)
        if server_override and server_override["crashed"]:
            print()
            cprint("Server Unavailable", "red")
            print()
            return

        banner = server_config["banner"]
        articles: list[Article] = server_config["contents"]
        self.__welcome(banner)
        options = list(map(lambda article: article["title"], articles))
        while True:
            print("Available pages:")
            user_input = show_menu(options)
            match user_input:
                case s if s.isdigit() and 1 <= int(s) <= len(options):
                    article: Article = articles[int(s) - 1]
                    print()
                    cprint(article["title"], "blue")
                    print()
                    print(article["content"])
                    print()
                    input("Press a key")
                    continue
                case _:
                    print()
                    cprint("Connection closed", "red")
                    break

    def mail_server(self, server_config: ServerConfig):
        banner = server_config["banner"]
        self.__welcome(banner)

    def chat_server(self, server_config: ServerConfig):
        banner = server_config["banner"]
        self.__welcome(banner)

    def gateway_server(self, server_config: ServerConfig):
        banner = server_config["banner"]
        self.__welcome(banner)

    def __welcome(self, banner: str):
        cprint(banner, "green")
        print()
