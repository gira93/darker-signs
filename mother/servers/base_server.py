from termcolor import cprint
from pyfiglet import Figlet
from system.mail import Mail
from system.dns import Dns
from system.player import Player
from system.utils import download_file, progress_bar, show_menu, upload_file
from mother.type_defs import (
    ServerConfig,
    WebServerConfig,
    FileServerConfig,
    MailServerConfig,
    ChatServerConfig,
    DbServerConfig,
    CommerceServerConfig,
    DbEntry,
    Email,
)


class BaseServer:
    def __init__(self, root_path: str, mail: Mail, dns: Dns, player: Player) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns
        self.player = player

    def file_server(self, server_config: FileServerConfig) -> None:
        base_commands = ["cat", "ls", "download", "help", "exit"]
        write_only_commands = ["rm", "upload"]

        id, config = self.__load_config(server_config)
        if config["crashed"]:
            print()
            cprint("Server Unavailable", "red")
            print()
            return

        available_commands = (
            base_commands + write_only_commands if config["writable"] else base_commands
        )
        self.__initialize_tools(server_config)
        self.__welcome(config["banner"], config["name"], config["font"])

        account = self.__authenticate(config)
        if not account:
            cprint("Disconnecting", "red")
            return

        files: dict[str, str] = dict(config["contents"][account])
        while True:
            filenames: list[str] = list(files.keys())
            command = input(f"{account} > ").split()
            com = command[0] if len(command) > 0 else ""
            param = command[1] if len(command) > 1 else ""
            if com in available_commands:
                match com:
                    case "cat":
                        if param in filenames:
                            print()
                            cprint(files[param], "blue")
                            print()
                        else:
                            cprint("File not found\n", "red")
                        continue
                    case "ls":
                        print()
                        cprint("  ".join(filenames), "blue")
                        print()
                        continue
                    case "download":
                        if param in filenames:
                            print()
                            cprint(f"Downloading {param}...", "green")
                            download_file(f"{self.root_path}/{param}", files[param])
                            print()
                        else:
                            cprint("File not found\n", "red")
                        continue
                    case "rm":
                        if param in filenames:
                            print()
                            cprint(f"{param} removed\n", "red")
                            files.pop(param, None)
                            if param == "kernel.sys":
                                config["crashed"] = True
                                print()
                                cprint("Kernel changed", "yellow")
                                cprint("Rebooting", "yellow")
                                progress_bar()
                                cprint("KERNEL MISSING", "red")
                                cprint("Connection closed by remote host", "red")
                                return
                        else:
                            cprint("File not found", "red")
                        continue
                    case "upload":
                        uploaded_file = upload_file(f"{self.root_path}/{param}")
                        print()
                        if uploaded_file:
                            cprint(f"{param} uploaded\n", "green")
                            files[param] = ""
                        else:
                            cprint("File not found in local machine\n", "red")
                        continue
                    case "help":
                        print("Available commands:")
                        print(" ".join(available_commands))
                        print()
                        continue
                    case "exit":
                        config["contents"][account] = list(files.items())
                        self.player.add_or_update_server(id, config)
                        if "connection.log" in filenames:
                            print()
                            cprint("Connection log file traced", "red")
                            print()
                        cprint("Disconnecting\n", "red")
                        break
            elif com == "":
                continue
            else:
                cprint("Command not found\n", "red")
                continue

    def web_server(self, server_config: WebServerConfig) -> None:
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

    def mail_server(self, server_config: MailServerConfig) -> None:
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

    def db_server(self, server_config: DbServerConfig) -> None:
        _, config = self.__load_config(server_config)

        self.__initialize_tools(server_config)
        self.__welcome(config["banner"], config["name"], config["font"])
        account = self.__authenticate(config)

        if not account:
            cprint("Disconnecting", "red")
            return

        entries: list[DbEntry] = config["contents"]
        while True:
            search_query = input("Type a search query (exit to disconnect): ")
            if search_query == "exit":
                print()
                cprint("Disconnecting", "red")
                break
            elif search_query == "":
                continue
            elif len(search_query) > 5:
                search_result = next(
                    (e for e in entries if search_query.lower() in e["title"].lower()),
                    None,
                )
                if search_result:
                    print()
                    cprint("Entry found\n", "green")
                    cprint(search_result["title"], "magenta")
                    print()
                    cprint(search_result["content"], "blue")
                    print()
                    input("Press a key")
                    continue
                else:
                    print()
                    cprint("No results found\n", "red")
                    continue
            else:
                cprint("Search query must be longer than 5 characters\n", "red")
                continue

    def chat_server(self, server_config: ChatServerConfig) -> None:
        pass

    def commerce_server(self, server_config: CommerceServerConfig) -> None:
        pass

    def gateway_server(self) -> None:
        print()
        cprint("This is a gateway server\nDirect connections are disabled\n", "red")
        return

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
            (
                pw == "rootbreaker"
                and self.player.has_tool("rootbreaker")
                and server_config["hack_tool"] == "rootbreaker"
            )
            or (
                pw == "rootbreaker2"
                and self.player.has_tool("rootbreaker2")
                and server_config["hack_tool"] == "rootbreaker2"
            )
            or (
                pw == "rootbreaker3"
                and self.player.has_tool("rootbreaker3")
                and server_config["hack_tool"] == "rootbreaker3"
            )
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
