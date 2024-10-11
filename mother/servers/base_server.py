from typing import TypedDict
from termcolor import cprint
from pyfiglet import Figlet
from system.mail import Mail
from system.dns import Dns
from system.player import Player
from system.utils import progress_bar, show_menu

Email = TypedDict("Email", {"from": str, "subject": str, "content": str})
File = TypedDict("File", {"name": str, "content": str})
ChatMessage = TypedDict("ChatMessage", {"op": str, "content": str})
DbEntry = TypedDict("DbEntry", {"title": str, "content": str})


class ServerConfig(TypedDict):
    id: str
    name: str
    font: str | None
    banner: str
    writable: bool
    authentication: list[tuple[str, str]] | None
    crashed: bool
    hack_tool: str | None
    defense_tool: str | None


class WebServerConfig(ServerConfig):
    contents: list[DbEntry]


class FileServerConfig(ServerConfig):
    contents: list[File]


class MailServerConfig(ServerConfig):
    contents: dict[str, list[Email]]


class ChatServerConfig(ServerConfig):
    contents: list[ChatMessage]


class DbServerConfig(ServerConfig):
    contents: list[DbEntry]


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
        self.__welcome(config["banner"], config["name"], config["font"])
        articles: list[DbEntry] = config["contents"]
        options = list(map(lambda article: article["title"], articles))
        while True:
            print("Available articles:")
            user_input = show_menu(options)
            match user_input:
                case s if s.isdigit() and 1 <= int(s) <= len(options):
                    article: DbEntry = articles[int(s) - 1]
                    print()
                    cprint(article["title"], "blue")
                    print()
                    print(article["content"])
                    print()
                    input("Press a key")
                    continue
                case "nukelord" if self.player.has_tool("nukelord") and config[
                    "hack_tool"
                ] == "nukelord":
                    print()
                    cprint("NUKING", "red")
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
        id, config = self.__load_config(server_config)
        self.__initialize_tools(server_config)
        self.__welcome(config["banner"], config["name"], config["font"])
        account = self.__authenticate(config)

        if not account:
            cprint("Disconnecting", "red")
            return

        messages: list[Email] = config["contents"][account]
        while True:
            options = list(map(lambda message: message["subject"], messages))
            print("Inbox:")
            user_input = show_menu(options)
            match user_input:
                case s if s.isdigit() and 1 <= int(s) <= len(options):
                    message_index = int(s) - 1
                    message: Email = messages[message_index]
                    print()
                    cprint(f'From: {message["from"]}', "blue")
                    cprint(f'Subject: {message["subject"]}', "blue")
                    print()
                    print(message["content"])
                    print()
                    if config["writable"]:
                        message_option = show_menu(
                            ["Delete message"], "Go back", "Select an action"
                        )
                        match message_option:
                            case "1":
                                messages.pop(message_index)
                                config["contents"][account] = messages
                                self.player.add_or_update_server(id, config)
                                print()
                                cprint("Message deleted", "red")
                                input("Press a key")
                                continue
                            case _:
                                continue
                    else:
                        input("Press a key")
                        continue
                case "0":
                    print()
                    cprint("Connection closed", "red")
                    break
                case _:
                    continue

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

    def __welcome(self, banner: str, name: str, font: str = "standard"):
        f = Figlet(font)
        cprint(f.renderText(name), "blue")
        print()
        cprint(banner, "green")
        print()

    def __authenticate(self, server_config: dict) -> str | None:
        accounts: dict[str, str] = dict(server_config["authentication"])
        cprint("Login required", "yellow")
        print()
        user = input("Username: ")
        pw = input("Password: ")
        if user in accounts and pw == accounts[user]:
            print()
            cprint("Access granted", "green")
            print()
            return user
        elif (
            pw == "rootbreaker"
            and self.player.has_tool("rootbreaker")
            and server_config["hack_tool"] == "rootbreaker"
        ):
            print()
            cprint("CRACKING", "red")
            progress_bar()
            if user in accounts:
                print()
                cprint("Access granted", "green")
                print()
                cprint(f"Password is: {accounts[user]}", "yellow")
                return user
            else:
                print()
                cprint("User not found\nCracking failed", "red")
                print()
                return None
        else:
            print()
            cprint("Invalid username or password", "red")
            return None
