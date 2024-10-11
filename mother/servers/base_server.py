from typing import TypedDict
from termcolor import cprint
from system.mail import Mail
from system.dns import Dns
from system.player import Player
from system.utils import progress_bar, show_menu

Email = TypedDict("Email", {"from": str, "to": str, "content": str})
File = TypedDict("File", {"name": str, "content": str})
Article = TypedDict("Article", {"title": str, "content": str})
ChatMessage = TypedDict("ChatMessage", {"op": str, "content": str})


class ServerConfig(TypedDict):
    id: str
    banner: str
    writable: bool
    crashed: bool
    hack_tool: str | None
    defense_tool: str | None


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
        id, config = self.__load_config(server_config)
        if config["crashed"]:
            print()
            cprint("Server Unavailable", "red")
            print()
            return

        self.__initialize_tools(server_config)
        self.__welcome(config["banner"])
        articles: list[Article] = config["contents"]
        options = list(map(lambda article: article["title"], articles))
        while True:
            print("Available articles:")
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
                case "nukelord" if self.player.has_tool("nukelord"):
                    print()
                    cprint("NUKING", "red")
                    print()
                    progress_bar()
                    cprint("SERVER NUKED", "green")
                    cprint("Disconnecting", "red")
                    config["crashed"] = True
                    self.player.add_or_update_server(id, config)
                    break
                case "0":
                    print()
                    cprint("Connection closed", "red")
                    break
                case _:
                    continue

    def mail_server(self, server_config: ServerConfig):
        banner = server_config["banner"]
        self.__welcome(banner)

    def chat_server(self, server_config: ServerConfig):
        banner = server_config["banner"]
        self.__welcome(banner)

    def gateway_server(self, server_config: ServerConfig):
        banner = server_config["banner"]
        self.__welcome(banner)

    def __initialize_tools(self, server_config: ServerConfig) -> None:
        if server_config["hack_tool"] and self.player.has_tool(
            server_config["hack_tool"]
        ):
            cprint(
                f"{server_config['hack_tool'].capitalize()} armed and ready!", "yellow"
            )
            print()
        if server_config["defense_tool"] and self.player.has_tool(
            server_config["defense_tool"]
        ):
            cprint(f"{server_config['defense_tool'].capitalize()} running!", "green")
            print()

    def __load_config(self, server_config: ServerConfig) -> tuple[str, dict]:
        id = server_config["id"]
        server_override = self.player.get_server(id)
        config = server_override if server_override else dict(server_config)
        return (id, config)

    def __welcome(self, banner: str):
        cprint(banner, "green")
        print()
